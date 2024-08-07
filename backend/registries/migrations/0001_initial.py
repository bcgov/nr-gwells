# Generated by Django 2.1.8 on 2019-04-30 23:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import gwells.db_comments.model_mixins
import uuid

from registries import data_migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gwells', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vw_well_class',
            fields=[
                ('subactivity', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('class_desc', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Registries Well Class',
                'verbose_name_plural': 'Registries Well Classes',
                'db_table': 'vw_well_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccreditedCertificateCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('acc_cert_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Accredited Certificate UUID')),
                ('name', models.CharField(editable=False, max_length=100, verbose_name='Certificate Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Accredited Certificates',
                'db_table': 'registries_accredited_certificate_code',
                'ordering': ['registries_activity', 'cert_auth'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ActivityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('registries_activity_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Activity codes',
                'db_table': 'registries_activity_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ApplicationStatusCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('code', models.CharField(db_column='registries_application_status_code', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Application Status Codes',
                'db_table': 'registries_application_status_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='CertifyingAuthorityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('cert_auth_code', models.CharField(editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Certifying Authority Name')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Certifying Authorities',
                'db_table': 'registries_certifying_authority_code',
                'ordering': ['cert_auth_code'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('org_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Organization UUID')),
                ('name', models.CharField(max_length=200)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Town/City')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal Code')),
                ('main_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telephone number')),
                ('fax_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Fax number')),
                ('website_url', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email adddress')),
                ('province_state', models.ForeignKey(db_column='province_state_code', on_delete=django.db.models.deletion.PROTECT, related_name='companies', to='gwells.ProvinceStateCode', verbose_name='Province/State')),
            ],
            options={
                'verbose_name_plural': 'Organizations',
                'db_table': 'registries_organization',
                'ordering': ['name'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='OrganizationNote',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('org_note_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Company note UUID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(max_length=2000)),
                ('author', models.ForeignKey(db_column='user_guid', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Author reference')),
                ('organization', models.ForeignKey(db_column='org_guid', on_delete=django.db.models.deletion.PROTECT, related_name='notes', to='registries.Organization', verbose_name='Company reference')),
            ],
            options={
                'db_table': 'registries_organization_note',
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('person_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Person UUID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('well_driller_orcs_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='ORCS File # reference (in context of Well Driller).')),
                ('pump_installer_orcs_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='ORCS File # reference (in context of Pump Installer).')),
                ('contact_tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact telephone number')),
                ('contact_cell', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact cell number')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email address')),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': 'People',
                'db_table': 'registries_person',
                'ordering': ['first_name', 'surname'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='PersonNote',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('person_note_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Person note UUID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(max_length=2000)),
                ('author', models.ForeignKey(db_column='user_guid', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Author reference')),
                ('person', models.ForeignKey(db_column='person_guid', on_delete=django.db.models.deletion.PROTECT, related_name='notes', to='registries.Person', verbose_name='Person reference')),
            ],
            options={
                'db_table': 'registries_person_note',
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='ProofOfAgeCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('code', models.CharField(db_column='registries_proof_of_age_code', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'ProofOfAgeCodes',
                'db_table': 'registries_proof_of_age_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('registries_well_qualification_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Qualification / Well Class UUID')),
            ],
            options={
                'verbose_name_plural': 'Qualification codes',
                'db_table': 'registries_well_qualification',
                'ordering': ['subactivity', 'display_order'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('register_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register UUID')),
                ('registration_no', models.CharField(blank=True, max_length=15, null=True)),
                ('organization', models.ForeignKey(blank=True, db_column='organization_guid', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='registries.Organization')),
                ('person', models.ForeignKey(db_column='person_guid', on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='registries.Person')),
                ('registries_activity', models.ForeignKey(db_column='registries_activity_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ActivityCode')),
            ],
            options={
                'verbose_name_plural': 'Registrations',
                'db_table': 'registries_register',
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='Register_Note',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('register_note_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register Node UUID')),
                ('notes', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Registrar notes, for internal use only.')),
                ('registration', models.ForeignKey(db_column='register_guid', on_delete=django.db.models.deletion.PROTECT, related_name='notes', to='registries.Register', verbose_name='Register Reference')),
            ],
            options={
                'verbose_name_plural': 'Registrar Notes',
                'db_table': 'registries_register_note',
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='RegistriesApplication',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('application_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Register Application UUID')),
                ('file_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='ORCS File # reference.')),
                ('registrar_notes', models.CharField(blank=True, max_length=255, null=True, verbose_name='Registrar notes, for internal use only.')),
                ('reason_denied', models.CharField(blank=True, max_length=255, null=True, verbose_name='Free form text explaining reason for denial.')),
                ('primary_certificate_no', models.CharField(max_length=50)),
                ('application_recieved_date', models.DateField(blank=True, null=True)),
                ('application_outcome_date', models.DateField(blank=True, null=True)),
                ('application_outcome_notification_date', models.DateField(blank=True, null=True)),
                ('removal_date', models.DateField(blank=True, null=True)),
                ('current_status', models.ForeignKey(blank=True, db_column='registries_application_status_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.ApplicationStatusCode', verbose_name='Application Status Code Reference')),
                ('primary_certificate', models.ForeignKey(blank=True, db_column='acc_cert_guid', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.AccreditedCertificateCode', verbose_name='Certificate')),
                ('proof_of_age', models.ForeignKey(db_column='registries_proof_of_age_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.ProofOfAgeCode', verbose_name='Proof of age.')),
                ('registration', models.ForeignKey(db_column='register_guid', on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='registries.Register', verbose_name='Person Reference')),
            ],
            options={
                'verbose_name_plural': 'Applications',
                'db_table': 'registries_application',
                'ordering': ['primary_certificate_no'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='RegistriesRemovalReason',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('code', models.CharField(db_column='registries_removal_reason_code', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Registry Removal Reasons',
                'db_table': 'registries_removal_reason_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='SubactivityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('registries_subactivity_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('registries_activity', models.ForeignKey(db_column='registries_activity_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ActivityCode')),
            ],
            options={
                'verbose_name_plural': 'Subactivity codes',
                'db_table': 'registries_subactivity_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.CreateModel(
            name='WellClassCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_user', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('registries_well_class_code', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Well Classes',
                'db_table': 'registries_well_class_code',
                'ordering': ['display_order', 'description'],
            },
            bases=(models.Model, gwells.db_comments.model_mixins.DBComments),
        ),
        migrations.AddField(
            model_name='registriesapplication',
            name='removal_reason',
            field=models.ForeignKey(blank=True, db_column='registries_removal_reason_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.RegistriesRemovalReason', verbose_name='Removal Reason'),
        ),
        migrations.AddField(
            model_name='registriesapplication',
            name='subactivity',
            field=models.ForeignKey(db_column='registries_subactivity_code', on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='registries.SubactivityCode'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='subactivity',
            field=models.ForeignKey(db_column='registries_subactivity_code', on_delete=django.db.models.deletion.PROTECT, related_name='qualification_set', to='registries.SubactivityCode'),
        ),
        migrations.AddField(
            model_name='qualification',
            name='well_class',
            field=models.ForeignKey(db_column='registries_well_class_code', on_delete=django.db.models.deletion.PROTECT, to='registries.WellClassCode'),
        ),
        migrations.AddField(
            model_name='accreditedcertificatecode',
            name='cert_auth',
            field=models.ForeignKey(db_column='cert_auth_code', on_delete=django.db.models.deletion.PROTECT, to='registries.CertifyingAuthorityCode'),
        ),
        migrations.AddField(
            model_name='accreditedcertificatecode',
            name='registries_activity',
            field=models.ForeignKey(db_column='registries_activity_code', on_delete=django.db.models.deletion.PROTECT, to='registries.ActivityCode'),
        ),
        migrations.RunPython(
            code=data_migrations.insert_remove_reasons,
            reverse_code=data_migrations.revert_remove_reasons),
    ]