# Generated by Django 4.2 on 2023-04-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
