This repository is an archive of the KumaScript Templates (a.k.a. macros)
developed on [Mozilla Developer Network](https://developer.mozilla.org) from
2005 to 2016.  In December 2016, the macros and macro development moved to
the [KumaScript repository](https://github.com/mozilla/kumascript).

KumaScript macro authors were contacted in January 2017, and some elected to
use their real names and connect their edits to their GitHub accounts.
For the rest, and for authors we couldn't contact, we attributed the edits to
their usernames on MDN.

Other changes made in the conversion to git:
* MDN allows edits with no changes. If the files were unchanged, a git commit
  was not added.
* MDN encourages editors to "publish and continue editing", resulting in
  several changes with no change message. Multiple edits from the same author
  were consolidated into the last edit.

See the ``export_templates.py`` script for the exact algorithm. These changes
reduced the 14,245 MDN revisions to 8,699 git commits.

Thank you to the over 200 contributors who edited MDN templates over eleven
years!
