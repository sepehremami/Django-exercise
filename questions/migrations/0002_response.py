# Generated by Django 4.2 on 2023-04-21 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stackoverflow.user')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.questions')),
            ],
        ),
    ]
