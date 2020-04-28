# -*- coding: utf-8 -*-
# Extract template edits from the MDN database to git
# Designed to be imported in a Django shell, such as:
# import export_template; export_template.do_it()

from __future__ import print_function, unicode_literals
import csv
import os
import os.path
import subprocess
import sys
import unicodedata

from kuma.wiki.models import Document, Revision

FS_ENCODING = sys.getfilesystemencoding()


def do_it(csv_file_path='authors.csv', git_repo_path='macros'):
    """Export templates from an MDN database to a new git repository."""
    path = init_repo(git_repo_path)
    authors = load_authors_csv(csv_file_path)
    print('Loaded %d authors' % len(authors))
    revisions = scan_revisions()
    print('Loaded %d revisions' % len(revisions))
    gitify_revisions(revisions, authors, path)


def init_repo(git_repo_path):
    """Initialize a git repo in a new directory."""
    path = os.path.normpath(os.path.expanduser(git_repo_path))
    if os.path.exists(path):
        raise Exception("%s should not exist." % path)
    subprocess.check_call(["git", "init", path])
    orig_dir = os.getcwd()
    os.chdir(path)
    subprocess.check_call(
        ["git", "config", "user.email", "jwhitlock@mozilla.com"])
    subprocess.check_call(
        ["git", "config", "user.name", "John Whitlock"])
    os.chdir(orig_dir)
    return path


def load_authors_csv(csv_path):
    """
    Load a CSV of author data.

    A header row is expected, and these columns:
    * username: MDN username
    * name: user-selected name
    * email: user-selected email
    * responded: indication if user responded (ignored)
    """
    authors = {}
    with open(csv_path, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        first = True
        for row in reader:
            if first:
                assert row[0] == 'username'
                first = False
            else:
                username, name, email, responded = [
                    cell.decode('utf8') for cell in row]
                assert username not in authors
                authors[username] = "%s <%s>" % (name, email)
    return authors


def scan_revisions():
    """Gather template edit data and sort by creation date."""
    usernames = {}
    revisions = []
    templates = Document.objects.filter(is_template=True)
    for doc_id in templates.values_list('id', flat=True):
        doc = Document.objects.get(id=doc_id)
        locale = doc.locale
        for revision in doc.revisions.all():
            if revision.creator_id not in usernames:
                usernames[revision.creator_id] = revision.creator.username
            username = usernames[revision.creator_id]
            revisions.append((
                revision.created,
                doc.id,
                revision.id,
                locale,
                username))
    revisions.sort()
    return revisions


def gitify_revisions(revisions, authors, path):
    """
    Convert revision data to git commits.

    Mutliple edits to the same file without comment are combined
    to a single commit.

    Macro renames are handled as a deletion and an addition, relying
    on git to determine if it counts as a rename.
    """
    last_filenames = {}
    orig_dir = os.getcwd()
    os.chdir(path)
    try:
        last_change = [None] * 4
        for created, doc_id, rev_id, locale, username in revisions:
            # Extract data from the revision
            rev = Revision.objects.get(id=rev_id)
            author = authors.get(
                username,
                "%s <no-reply+%s@developer.mozilla.org>" %
                (username, username))
            comment = rev.comment.strip()
            created = rev.created
            last_fn = last_filenames.setdefault(
                doc_id, to_filename(locale, rev.slug))
            current_fn = to_filename(locale, rev.slug)

            # Should we commit the last change?
            old_doc_id, old_author, old_comment, old_created = last_change
            if (old_doc_id and (
                    (old_doc_id != doc_id) or
                    (old_author != author) or
                    (last_fn != current_fn))):
                commit(old_author, old_comment, old_created)
                last_change = [None] * 4

            # If a file was renamed, remove the old path
            # git will decide if it is an add/remove or a rename
            if last_fn != current_fn:
                subprocess.check_call([b"git", b"rm", last_fn])

            # Write the new contents to disk
            if not os.path.exists(locale):
                os.mkdir(locale)
            with open(current_fn, 'w') as macro_file:
                macro_file.write(normalize_content(rev.content))

            # Add the file to the index
            subprocess.check_call([b'git', b'add', current_fn])

            # Check if our encoding gymnastics were correct
            untracked = ['git', 'ls-files', '--others', '--exclude-standard']
            leftovers = subprocess.check_output(untracked)
            assert not leftovers.strip(), leftovers

            # Save the filename for next time
            last_filenames[doc_id] = current_fn

            # Commit the changes or save for next time
            if comment or (last_fn != current_fn):
                commit(author, comment, created)
                last_change = [None] * 4
            else:
                last_change = [doc_id, author, comment, created]
    finally:
        os.chdir(orig_dir)


def to_filename(locale, slug):
    """
    Convert a slug to a encoded filename.

    This works when writing files in Docker on a MacOS system.
    It may be different for other configurations.
    """
    assert slug.startswith("Template:")
    filename = slug.replace("Template:", "", 1).replace(':', '-') + '.ejs'
    path = os.path.join(locale, filename)
    try:
        fs_encoded = path.encode(FS_ENCODING)
    except UnicodeEncodeError:
        fs_encoded = unicodedata.normalize('NFD', path).encode('utf8')
    return fs_encoded


def normalize_content(raw_content):
    """Normalize macros to git format."""
    content = raw_content.replace('\r\n', '\n')
    if content and content[-1] != '\n':
        content += '\n'
    return content.encode('utf-8')


def encode_cmd(*command):
    """Encode a command list for subprocess."""
    return [arg.encode('utf8') for arg in command]


def commit(author, comment, created):
    """Commit the index, if there is anything to commit."""
    # If there are no changes, don't commit it
    command = ['git', 'status', '--short']
    work_to_do = subprocess.check_output(encode_cmd(*command))
    if not work_to_do.strip():
        return

    # Setup the commit
    command = ['git', 'commit']
    command.append('--author="%s"' % author)
    if comment:
        command.extend(['-m', comment])
    else:
        command.extend(['--message=', '--allow-empty-message'])
    command.append('--date=%s' % created.isoformat())

    # Set the committer as the author, rather then jwhitlock
    env = os.environ.copy()
    name, email = author.strip().split('<')
    email = email[:-1]
    env[b'GIT_COMMITTER_NAME'] = name.encode('utf8')
    env[b'GIT_COMMITTER_EMAIL'] = email.encode('utf8')
    env[b'GIT_COMMITTER_DATE'] = created.isoformat()
    subprocess.check_call(encode_cmd(*command), env=env)

    # Double-check that the working copy is clean
    leftovers = subprocess.check_output(['git', 'status', '--short'])
    assert not leftovers.strip(), leftovers
