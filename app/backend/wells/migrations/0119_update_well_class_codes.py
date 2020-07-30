# Generated by Django 2.2.13 on 2020-07-28 20:28

from django.db import migrations

UPDATE_WELLS = """
    UPDATE well SET well_class_code = 'DEW_DRA' WHERE well_class_code = 'DEWATERING';
    UPDATE well SET well_class_code = 'DEW_DRA' WHERE well_class_code = 'DRAINAGE';
    UPDATE well SET well_subclass_guid = '46300f40-fc6b-4c77-a58e-74472cd69f5d' WHERE well_subclass_guid = '3fa27b8a-4ca1-11e7-b114-b2f933d5fe66';
    UPDATE well SET well_subclass_guid = '46300f40-fc6b-4c77-a58e-74472cd69f5d' WHERE well_subclass_guid = '5a314ee0-47e7-11e7-a919-92ebcb67fe33';
    UPDATE well SET well_subclass_guid = '6f124222-ab9e-43c7-89e4-a2b8673611cf' WHERE well_subclass_guid = '5a314404-47e7-11e7-a919-92ebcb67fe33';
"""

UPDATE_SUBMISSIONS = """
    UPDATE activity_submission SET well_class_code = 'DEW_DRA' WHERE well_class_code = 'DEWATERING';
    UPDATE activity_submission SET well_class_code = 'DEW_DRA' WHERE well_class_code = 'DRAINAGE';
    UPDATE activity_submission SET well_subclass_guid = '46300f40-fc6b-4c77-a58e-74472cd69f5d' WHERE well_subclass_guid = '3fa27b8a-4ca1-11e7-b114-b2f933d5fe66';
    UPDATE activity_submission SET well_subclass_guid = '46300f40-fc6b-4c77-a58e-74472cd69f5d' WHERE well_subclass_guid = '5a314ee0-47e7-11e7-a919-92ebcb67fe33';
    UPDATE activity_submission SET well_subclass_guid = '6f124222-ab9e-43c7-89e4-a2b8673611cf' WHERE well_subclass_guid = '5a314404-47e7-11e7-a919-92ebcb67fe33';
"""

EXPIRE_DEWATERING_DRAINAGE_CODES = """
    UPDATE well_class_code SET expiry_date = '2020-07-28 00:00:00+00' WHERE well_class_code = 'DEWATERING';
    UPDATE well_class_code SET expiry_date = '2020-07-28 00:00:00+00' WHERE well_class_code = 'DRAINAGE';
"""

class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0118_add_well_class_code'),
    ]

    operations = [
        migrations.RunSQL([
            UPDATE_WELLS,
            UPDATE_SUBMISSIONS,
            EXPIRE_DEWATERING_DRAINAGE_CODES,
        ]),
    ]