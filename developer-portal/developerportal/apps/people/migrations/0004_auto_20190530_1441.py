# Generated by Django 2.2.1 on 2019-05-30 14:41

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [("people", "0003_auto_20190530_1437")]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="labels",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True,
                related_name="_person_labels_+",
                to="topics.Topic",
                verbose_name="Topics interested in",
            ),
        )
    ]
