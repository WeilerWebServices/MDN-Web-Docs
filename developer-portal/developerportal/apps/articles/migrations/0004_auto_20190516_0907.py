# Generated by Django 2.2.1 on 2019-05-16 09:07

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("articles", "0003_article_intro")]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="intro",
            field=wagtail.core.fields.RichTextField(default="", verbose_name="Intro"),
        )
    ]
