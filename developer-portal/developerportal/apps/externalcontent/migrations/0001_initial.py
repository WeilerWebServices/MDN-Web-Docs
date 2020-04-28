# Generated by Django 2.2.3 on 2019-07-04 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural")
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalContent",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("url", models.URLField(blank=True, default="", max_length=2048)),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        )
    ]
