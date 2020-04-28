# Generated by Django 2.2.1 on 2019-05-16 13:03

import datetime
from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("articles", "0005_auto_20190516_1236")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="date",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Article date"
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="intro",
            field=wagtail.core.fields.RichTextField(default="", verbose_name="Intro"),
        ),
    ]