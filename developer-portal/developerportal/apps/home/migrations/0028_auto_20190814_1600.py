# Generated by Django 2.2.4 on 2019-08-14 16:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [("home", "0027_auto_20190813_1503")]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="featured",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "article",
                        wagtail.core.blocks.PageChooserBlock(
                            page_type=[
                                "articles.Article",
                                "externalcontent.ExternalArticle",
                            ]
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
        )
    ]
