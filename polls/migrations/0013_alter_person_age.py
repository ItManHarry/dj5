# Generated by Django 5.0.1 on 2024-02-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
