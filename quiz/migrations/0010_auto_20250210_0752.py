# Generated by Django 3.1.12 on 2025-02-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20250210_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.TextField(default='New Quiz'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
