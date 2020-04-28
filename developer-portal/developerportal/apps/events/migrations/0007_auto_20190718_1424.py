# Generated by Django 2.2.3 on 2019-07-18 14:24

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0002_auto_20150616_2121"),
        ("events", "0006_auto_20190712_1231"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="card_venue"),
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Location details (city and country), displayed on event cards",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="venue",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Full address of the event venue, displayed on the event detail page",
                max_length=250,
            ),
        ),
        migrations.CreateModel(
            name="EventsTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="events.Events",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events_eventstag_items",
                        to="taggit.Tag",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="events",
            name="keywords",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="events.EventsTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]