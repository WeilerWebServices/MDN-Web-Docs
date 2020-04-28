# Generated by Django 2.2.1 on 2019-07-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0008_auto_20190625_1119")]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="button_text",
            field=models.CharField(blank=True, default="", max_length=30),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="button_url",
            field=models.URLField(blank=True, default="", max_length=140),
        ),
    ]