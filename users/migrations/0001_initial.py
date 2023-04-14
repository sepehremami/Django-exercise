# Generated by Django 4.1.6 on 2023-04-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athur',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('address', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('url', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
