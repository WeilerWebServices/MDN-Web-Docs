# Generated by Django 2.2.3 on 2019-08-02 13:37

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [("people", "0021_auto_20190731_1057")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="websites",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "website",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("url", wagtail.core.blocks.URLBlock(label="URL")),
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "icon",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        )
    ]
