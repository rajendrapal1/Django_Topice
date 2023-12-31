# Generated by Django 4.2.2 on 2023-07-04 11:02

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_news', '0003_alter_model_class_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_class',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='subject', unique=True),
        ),
    ]
