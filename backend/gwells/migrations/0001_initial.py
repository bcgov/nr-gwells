# Generated by Django 2.1.8 on 2019-04-30 23:59

import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import gwells.db_comments.model_mixins
import uuid

from gwells import data_migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BedrockMaterialCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('bedrock_material_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bedrock_material_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='BedrockMaterialDescriptorCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('bedrock_material_descriptor_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bedrock_material_descriptor_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Border',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('se_a_c_flg', models.CharField(max_length=254, null=True)),
                ('obejctid', models.FloatField()),
                ('shape', models.FloatField(null=True)),
                ('length_m', models.FloatField()),
                ('oic_number', models.CharField(max_length=7, null=True)),
                ('area_sqm', models.FloatField()),
                ('upt_date', models.CharField(max_length=20)),
                ('upt_type', models.CharField(max_length=50)),
                ('chng_org', models.CharField(max_length=30)),
                ('aa_parent', models.CharField(max_length=100)),
                ('aa_type', models.CharField(max_length=50)),
                ('aa_id', models.BigIntegerField()),
                ('aa_name', models.CharField(max_length=100)),
                ('abrvn', models.CharField(max_length=40)),
                ('bdy_type', models.CharField(max_length=20)),
                ('oic_year', models.CharField(max_length=4, null=True)),
                ('afctd_area', models.CharField(max_length=120, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4269)),
            ],
        ),
        migrations.CreateModel(
            name='LithologyColourCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('lithology_colour_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, verbose_name='Colour Description')),
            ],
            options={
                'db_table': 'lithology_colour_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='LithologyDescriptionCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('lithology_description_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='Code')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
            options={
                'db_table': 'lithology_description_code',
                'ordering': ['display_order'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='LithologyHardnessCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('lithology_hardness_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, verbose_name='Hardness')),
            ],
            options={
                'db_table': 'lithology_hardness_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='LithologyMaterialCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('lithology_material_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, verbose_name='Code')),
                ('description', models.CharField(max_length=255, verbose_name='Material Description')),
            ],
            options={
                'db_table': 'lithology_material_code',
                'ordering': ['display_order'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='LithologyMoistureCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('lithology_moisture_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'lithology_moisture_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='LithologyStructureCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('lithology_structure_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'lithology_structure_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='OnlineSurvey',
            fields=[
                ('survey_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('survey_introduction_text', models.TextField(blank=True, max_length=200, null=True, verbose_name='Introduction Text')),
                ('survey_link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('survey_enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('survey_page', models.CharField(choices=[('w', 'well'), ('r', 'registry'), ('s', 'search'), ('a', 'aquifer')], default='w', max_length=1, verbose_name='Page')),
                ('effective_date', models.DateField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
            ],
            options={
                'db_table': 'online_survey',
                'ordering': ['effective_date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='ProvinceStateCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('province_state_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField(db_index=True)),
            ],
            options={
                'db_table': 'province_state_code',
                'ordering': ['display_order'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ScreenAssemblyTypeCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('screen_assembly_type_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'screen_assembly_type_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ScreenBottomCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('screen_bottom_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'screen_bottom_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ScreenIntakeMethodCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('screen_intake_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'screen_intake_method_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ScreenMaterialCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('screen_material_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'screen_material_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ScreenOpeningCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('screen_opening_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'screen_opening_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ScreenTypeCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('screen_type_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'screen_type_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='SurficialMaterialCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('surficial_material_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'surficial_material_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('survey_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('survey_introduction_text', models.CharField(blank=True, max_length=250, null=True, verbose_name='Introduction Text')),
                ('survey_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Link')),
                ('survey_enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('survey_page', models.CharField(choices=[('w', 'well'), ('r', 'registry'), ('s', 'search'), ('a', 'aquifer')], default='w', max_length=1, verbose_name='Page')),
            ],
            options={
                'db_table': 'gwells_survey',
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.RunPython(data_migrations.border_data, reverse_code=data_migrations.reverse_border_data),
    ]
