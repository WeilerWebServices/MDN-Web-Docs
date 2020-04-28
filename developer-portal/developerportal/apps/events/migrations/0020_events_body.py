# Generated by Django 2.2.8 on 2019-12-18 13:34

import developerportal.apps.common.fields
from django.db import migrations
import wagtail.core.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_add_social_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='body',
            field=developerportal.apps.common.fields.CustomStreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=('bold', 'blockquote', 'code', 'h2', 'h3', 'h4', 'hr', 'image', 'italic', 'link', 'ol', 'ul'))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='External URL to link to instead of a page.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('embed_html', wagtail.core.blocks.RawHTMLBlock(help_text='Warning: be careful what you paste here, since this field could introduce XSS (or similar) bugs. This field is meant solely for third-party embeds.')), ('code_snippet', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('css', 'CSS'), ('go', 'Go'), ('html', 'HTML'), ('js', 'JavaScript'), ('python', 'Python'), ('rust', 'Rust'), ('ts', 'TypeScript')])), ('code', wagtail.core.blocks.TextBlock())]))], default=None, help_text='Main page body content. Supports rich text, images, embed via URL, embed via HTML, and inline code snippets'),
        ),
    ]
