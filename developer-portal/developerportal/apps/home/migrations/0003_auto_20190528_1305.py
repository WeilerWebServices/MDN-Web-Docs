# Generated by Django 2.2.1 on 2019-05-28 13:05

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("home", "0002_create_homepage")]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="button_text",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AddField(
            model_name="homepage",
            name="button_url",
            field=models.URLField(default="", max_length=140),
        ),
        migrations.AddField(
            model_name="homepage",
            name="intro",
            field=wagtail.core.fields.RichTextField(default=""),
        ),
        migrations.AddField(
            model_name="homepage",
            name="subtitle",
            field=models.CharField(default="", max_length=140),
        ),
    ]
