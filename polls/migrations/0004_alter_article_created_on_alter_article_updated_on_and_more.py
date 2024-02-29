# Generated by Django 5.0.1 on 2024-01-24 02:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_article_options_article_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]