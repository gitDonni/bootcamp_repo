# Generated by Django 5.0.6 on 2024-06-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
