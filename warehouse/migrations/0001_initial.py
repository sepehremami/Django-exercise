# Generated by Django 4.1.6 on 2023-04-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('code', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
