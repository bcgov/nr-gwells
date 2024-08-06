# Generated by Django 2.1.8 on 2019-05-02 23:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import gwells.db_comments.model_mixins
import wells.data_migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0001_squashed_0079_auto_20190506_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='WellDisinfectedCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('well_disinfected_code', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'well_disinfected_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.RunPython(
            code=wells.data_migrations.load_well_disinfected_codes,
            reverse_code=wells.data_migrations.unload_well_disinfected_codes,
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='well_disinfected_status',
            field=models.ForeignKey(blank=True, db_column='well_disinfected_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='wells.WellDisinfectedCode', verbose_name='Well Disinfected Code'),
        ),
        migrations.AddField(
            model_name='well',
            name='well_disinfected_status',
            field=models.ForeignKey(blank=True, db_column='well_disinfected_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='wells.WellDisinfectedCode', verbose_name='Well Disinfected Code'),
        ),
    ]
