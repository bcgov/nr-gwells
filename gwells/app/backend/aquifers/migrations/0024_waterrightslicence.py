# Generated by Django 2.2.1 on 2019-05-25 23:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import gwells.db_comments.model_mixins


class Migration(migrations.Migration):

    dependencies = [
        ('aquifers', '0023_delete_waterrightslicence'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterRightsLicence',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('wrl_sysid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Water Rights Licence System ID')),
                ('licence_number', models.BigIntegerField(db_index=True)),
                ('quantity_flag', models.CharField(choices=[('T', 'T'), ('M', 'M'), ('D', 'D'), ('P', 'P')], default='T', max_length=1)),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Quanitity')),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('purpose', models.ForeignKey(blank=True, db_column='water_rights_purpose_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='licences', to='aquifers.WaterRightsPurpose', verbose_name='Water Rights Purpose Reference')),
            ],
            options={
                'verbose_name_plural': 'Aquifer Licences',
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
    ]
