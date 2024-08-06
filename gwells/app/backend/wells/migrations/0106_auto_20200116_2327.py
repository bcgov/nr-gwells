# Generated by Django 2.2.9 on 2020-01-16 23:27

from django.db import migrations


INSERT_DRILLING_COMPANIES_INTO_ORG = """
    INSERT INTO registries_organization (create_user, create_date, update_user, update_date, org_guid, name, effective_date, expiry_date, province_state_code)
        SELECT create_user, create_date, update_user, update_date, drilling_company_guid, name, '2018-01-01 00:00:00', '9999-12-31 00:00:00', 'BC' FROM drilling_company;
"""

# Update any wells to use the same GUID which will point to the drilling companies inserted above
UPDATE_WELL_ORG_TO_POINT_TO_OLD_DRILLING_COMPANY_GUIDS = """
    UPDATE well
    SET org_of_person_responsible_guid = drilling_company_guid
    WHERE org_of_person_responsible_guid IS NULL;
"""

# Update any legacy submissions to use the same GUID which will point to the drilling companies inserted for the FK-ed well
UPDATE_LEGACY_SUBMISSION_TO_OLD_DRILLING_COMPANY_GUID = """
    UPDATE activity_submission AS s
    SET org_of_person_responsible_guid = w.drilling_company_guid
    FROM well AS w
    WHERE
        s.well_tag_number = w.well_tag_number AND
        s.org_of_person_responsible_guid IS NULL AND
        s.well_activity_code = 'LEGACY';
"""

class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0105_auto_20200109_0031'),
    ]

    operations = [
        migrations.RunSQL(
            INSERT_DRILLING_COMPANIES_INTO_ORG,
        ),
        migrations.RunSQL(
            UPDATE_WELL_ORG_TO_POINT_TO_OLD_DRILLING_COMPANY_GUIDS,
        ),
        migrations.RunSQL(
            UPDATE_LEGACY_SUBMISSION_TO_OLD_DRILLING_COMPANY_GUID
        ),
    ]
