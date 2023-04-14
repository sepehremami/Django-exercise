# Generated by Django 4.1.6 on 2023-04-14 09:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.athur')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Warehousebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='warehouse',
            field=models.ManyToManyField(through='library.Warehousebook', to='warehouse.warehouse'),
        ),
    ]