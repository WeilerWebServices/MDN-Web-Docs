# Generated by Django 2.2.1 on 2019-05-16 15:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [("articles", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", wagtail.core.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                ],
                default=None,
            ),
        )
    ]