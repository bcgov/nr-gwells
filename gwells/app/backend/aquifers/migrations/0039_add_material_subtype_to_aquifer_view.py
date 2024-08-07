# Generated by Django 2.2.28 on 2023-02-24 22:17

from django.db import migrations

UPDATE_GWELLS_AQUIFER_VIEW_SQL = """
    DROP VIEW postgis_ftw.gwells_aquifer_view;
    CREATE VIEW postgis_ftw.gwells_aquifer_view AS
        SELECT
            aquifer_id,
            aquifer_name,
            area,
            retire_date <= NOW() AS is_retired,
            aquifer.effective_date <= NOW() AND aquifer.expiry_date >= NOW() AS is_published,
            geom,
            aquifer_material_code.description as material_type,
            aquifer_subtype_code as subtype
        FROM aquifer
        JOIN aquifer_material_code
        ON aquifer_material_code.aquifer_material_code = aquifer.aquifer_material_code
        WHERE geom IS NOT NULL;
        GRANT SELECT ON postgis_ftw.gwells_aquifer_view TO ftw_reader;
"""

REVERSE_UPDATE_GWELLS_AQUIFER_VIEW_SQL = """
    DROP VIEW postgis_ftw.gwells_aquifer_view;
    CREATE VIEW postgis_ftw.gwells_aquifer_view AS
        SELECT
            aquifer_id,
            aquifer_name,
            area,
            retire_date <= NOW() AS is_retired,
            effective_date <= NOW() AND expiry_date >= NOW() AS is_published,
            geom
        FROM aquifer
        WHERE geom IS NOT NULL;
        GRANT SELECT ON postgis_ftw.gwells_aquifer_view TO ftw_reader;
"""

class Migration(migrations.Migration):

    dependencies = [
        ('aquifers', '0038_aquifer_resource_section_update'),
    ]

    operations = [
        migrations.RunSQL(
          UPDATE_GWELLS_AQUIFER_VIEW_SQL,
          REVERSE_UPDATE_GWELLS_AQUIFER_VIEW_SQL
        )
    ]
