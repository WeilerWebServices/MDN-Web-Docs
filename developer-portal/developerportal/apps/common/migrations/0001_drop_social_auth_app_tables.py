# Generated by Django 2.2.6 on 2019-10-24 12:27
"""
Drop django-social-auth tables from the database, if they still exist,
following the removal of it from the codebase.
"""

import logging

from django.db import connection
from django.db import migrations

logger = logging.getLogger(__name__)


def drop_social_auth_tables(apps, schema_migration):
    # We're expecting them to be empty, with no cascading side-effects
    table_names = [
        "social_auth_usersocialauth",
        "social_auth_partial",
        "social_auth_association",
        "social_auth_code",
        "social_auth_nonce",
    ]
    logger.info("Dropping redundant DB tables %s", table_names)
    with connection.cursor() as cursor:
        for table_name in table_names:
            query = f"DROP TABLE IF EXISTS {table_name}"
            logger.info(f"Query: {query}")
            cursor.execute(query)


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        # DISABLED BECAUSE WE NO LONGER NEED IT, BUT KEPT FOR REFERENCE
        # migrations.RunPython(drop_social_auth_tables, migrations.RunPython.noop)
        # migrations.RunPython(drop_social_auth_tables, migrations.RunPython.noop)
    ]
