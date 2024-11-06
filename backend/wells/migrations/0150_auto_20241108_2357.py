# Generated by Django 3.2.4 on 2024-11-08 23:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
        ('wells', '0149_add_well_status_to_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='WellLicence',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('well_id', models.IntegerField()),
                ('waterrightslicence_id', models.IntegerField()),
            ],
            options={
                'db_table': 'well_licences',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='aquiferparameters',
            name='private',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='artesian_conditions',
            field=models.BooleanField(null=True, verbose_name='Artesian Conditions'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='artesian_pressure',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Artesian Pressure'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='artesian_pressure_head',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Artesian Pressure head'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='well_activity_type',
            field=models.ForeignKey(db_column='well_activity_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='submissions.wellactivitycode', verbose_name='Type of Work'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='well_orientation',
            field=models.BooleanField(choices=[(True, 'vertical'), (False, 'horizontal')], null=True, verbose_name='Orientation of Well'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='well_publication_status',
            field=models.ForeignKey(db_column='well_publication_status_code', default='Published', null=True, on_delete=django.db.models.deletion.PROTECT, to='wells.wellpublicationstatuscode', verbose_name='Well Publication Status'),
        ),
        migrations.AlterField(
            model_name='aquiferparameters',
            name='analysis_method',
            field=models.ForeignKey(blank=True, db_column='analysis_method_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='wells.analysismethodcode', verbose_name='Analysis Method'),
        ),
        migrations.AlterField(
            model_name='aquiferparameters',
            name='aquifer_parameters_guid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='aquiferparameters',
            name='pumping_test_description',
            field=models.ForeignKey(blank=True, db_column='pumping_test_description_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='wells.pumpingtestdescriptioncode', verbose_name='Testing Type'),
        ),
        migrations.AlterField(
            model_name='fieldsprovided',
            name='alternative_specs_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fieldsprovided',
            name='hydro_fracturing_performed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='well',
            name='artesian_conditions',
            field=models.BooleanField(default=False, verbose_name='Artesian Conditions'),
        ),
        migrations.AlterField(
            model_name='well',
            name='artesian_pressure_head',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Artesian Pressure head'),
        ),
        migrations.AlterField(
            model_name='well',
            name='cross_referenced_by',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Internal team member who cross referenced well.'),
        ),
        migrations.AlterField(
            model_name='well',
            name='cross_referenced_date',
            field=models.DateTimeField(null=True, verbose_name='Cross Referenced Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='distance_to_pid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Distance to PID'),
        ),
        migrations.AlterField(
            model_name='well',
            name='geocode_distance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Geocode Distance'),
        ),
        migrations.AlterField(
            model_name='well',
            name='natural_resource_region',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Natural Resource Region'),
        ),
    ]