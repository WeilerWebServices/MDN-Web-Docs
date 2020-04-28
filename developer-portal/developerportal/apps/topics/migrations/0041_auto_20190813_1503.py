# Generated by Django 2.2.4 on 2019-08-13 15:03

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [("topics", "0040_auto_20190813_1302")]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="description",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Optional short text description, max. 400 characters",
                max_length=400,
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="featured",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "article",
                        wagtail.core.blocks.PageChooserBlock(
                            page_type=[
                                "articles.Article",
                                "externalcontent.ExternalArticle",
                            ],
                            required=False,
                        ),
                    ),
                    (
                        "external_page",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("url", wagtail.core.blocks.URLBlock()),
                                ("title", wagtail.core.blocks.CharBlock()),
                                (
                                    "description",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                help_text="Optional space for featured articles, max. 4",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="tabbed_panels",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "panel",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("title", wagtail.core.blocks.CharBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("description", wagtail.core.blocks.TextBlock()),
                                ("button_text", wagtail.core.blocks.CharBlock()),
                                (
                                    "page_link",
                                    wagtail.core.blocks.PageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "external_link",
                                    wagtail.core.blocks.URLBlock(
                                        help_text="External URL to link to instead of a page.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                help_text="Optional tabbed panels for linking out to other resources, max. 3",
                null=True,
                verbose_name="Tabbed panels",
            ),
        ),
    ]
