# Generated by Django 2.2.1 on 2019-05-30 13:34

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0001_squashed_0021"),
        ("topics", "0002_topics"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                ("job_title", models.CharField(max_length=250)),
                ("intro", wagtail.core.fields.RichTextField(default="")),
                ("twitter", models.CharField(max_length=250)),
                ("facebook", models.CharField(max_length=250)),
                ("linkedin", models.CharField(max_length=250)),
                ("github", models.CharField(max_length=250)),
                ("email", models.CharField(max_length=250)),
                (
                    "intro_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "labels",
                    modelcluster.fields.ParentalManyToManyField(
                        blank=True, related_name="_person_labels_+", to="topics.Topic"
                    ),
                ),
                (
                    "profile_picture",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        )
    ]
