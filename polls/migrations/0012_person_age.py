# Generated by Django 5.0.1 on 2024-02-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_proxyemployee2_alter_proxyemployee1_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]