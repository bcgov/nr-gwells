# Generated by Django 2.2.9 on 2020-01-30 21:21

from django.db import migrations

import registries.data_migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registries', '0002_auto_20200120_1617'),
    ]

    operations = [
        migrations.RunPython(
            code=registries.data_migrations.load_activity_codes,
            reverse_code=registries.data_migrations.unload_activity_codes,
        ),
        migrations.RunPython(
            code=registries.data_migrations.load_subactivity_codes,
            reverse_code=registries.data_migrations.unload_subactivity_codes,
        ),
    ]
