# Generated by Django 2.2.18 on 2021-03-30 20:09

from django.db import migrations

"""
NOTES: This ticket contains 3 migrations, just to keep things as clear as possible.
The first migration updates the views to either return null for the column well.surface_seal_length being removed
or to exclude it completely for version 2 related export and databc
1 of 3
"""

"""
Well V1
    note on extra joins:
    well_licences: any well having at least 1 licence entry will be marked as Licensed.
"""
CREATE_EXPORT_WELL_VIEW_SQL_V1 = """
drop view if exists export_well_v1_view;
create view export_well_v1_view as 
select 
    well.well_tag_number as well_tag_number, 
    identification_plate_number as identification_plate_number,
    well_identification_plate_attached as well_identification_plate_attached,
    well_status_code as well_status_code, 
    well.well_class_code as well_class_code,
    wsc.well_subclass_code as well_subclass,
    CASE WHEN licence_q.cur_licences > 0 THEN 'LICENSED' ELSE 'UNLICENSED' END as licenced_status_code,
    intended_water_use_code as intended_water_use_code,
    observation_well_number as observation_well_number, 
    obs_well_status_code as obs_well_status_code, 
    water_supply_system_name as water_supply_system_name,
    water_supply_system_well_name as water_supply_system_well_name,
    well.street_address as street_address, 
    well.city as city, 
    legal_lot as legal_lot, 
    legal_plan as legal_plan, 
    legal_district_lot as legal_district_lot, 
    legal_block as legal_block,
    legal_section as legal_section, 
    legal_township as legal_township, 
    legal_range as legal_range,
    land_district_code as land_district_code,
    legal_pid as legal_pid,
    well_location_description as well_location_description,
    st_y(well.geom) as latitude, 
    st_x(well.geom) as longitude, 
    utm_zone_code as utm_zone_code, 
    utm_northing as utm_northing, 
    utm_easting as utm_easting,
    coordinate_acquisition_code as coordinate_acquisition_code, 
    bcgs_id as bcgs_id,
    construction_start_date as construction_start_date, 
    construction_end_date as construction_end_date, 
    alteration_start_date as alteration_start_date,
    alteration_end_date as alteration_end_date, 
    decommission_start_date as decommission_start_date, 
    decommission_end_date as decommission_end_date,
    driller_name as driller_name, 
    consultant_name as consultant_name, 
    consultant_company as consultant_company,
    diameter as diameter, 
    total_depth_drilled as total_depth_drilled, 
    finished_well_depth as finished_well_depth, 
    final_casing_stick_up as final_casing_stick_up,
    bedrock_depth as bedrock_depth, 
    ground_elevation as ground_elevation, 
    ground_elevation_method_code as ground_elevation_method_code, 
    static_water_level as static_water_level,
    well_yield as well_yield,
    well_yield_unit_code as well_yield_unit_code,
    artesian_flow as artesian_flow, 
    artesian_pressure as artesian_pressure, 
    well_cap_type as well_cap_type, 
    well_disinfected_code as well_disinfected_code,
    well_orientation_code as well_orientation_code,
    alternative_specs_submitted as alternative_specs_submitted,
    surface_seal_material_code as surface_seal_material_code, 
    surface_seal_method_code as surface_seal_method_code, 
    null as surface_seal_length, 
    surface_seal_depth as surface_seal_depth,
    backfill_type as backfill_type,
    backfill_depth as backfill_depth,
    liner_material_code as liner_material_code, 
    liner_diameter as liner_diameter, 
    liner_thickness as liner_thickness, 
    surface_seal_thickness as surface_seal_thickness,
    liner_from as liner_from, 
    liner_to as liner_to,
    screen_intake_method_code as screen_intake_method_code, 
    screen_type_code as screen_type_code, 
    screen_material_code as screen_material_code,
    other_screen_material as other_screen_material, 
    screen_information as screen_information,
    screen_opening_code as screen_opening_code, 
    screen_bottom_code as screen_bottom_code, 
    other_screen_bottom as other_screen_bottom,
    filter_pack_from as filter_pack_from,
    filter_pack_to as filter_pack_to, 
    filter_pack_material_code as filter_pack_material_code,
    filter_pack_thickness as filter_pack_thickness,
    filter_pack_material_size_code as filter_pack_material_size_code,
    development_hours as development_hours, 
    development_notes as development_notes,
    water_quality_colour as water_quality_colour, 
    water_quality_odour as water_quality_odour,
    yield_estimation_method_code as yield_estimation_method_code,
    yield_estimation_rate as yield_estimation_rate,
    yield_estimation_duration as yield_estimation_duration, 
    static_level_before_test as static_level_before_test, 
    drawdown as drawdown,
    hydro_fracturing_performed as hydro_fracturing_performed, 
    hydro_fracturing_yield_increase as hydro_fracturing_yield_increase,
    decommission_reason as decommission_reason, 
    decommission_method_code as decommission_method_code, 
    decommission_details as decommission_details, 
    decommission_sealant_material as decommission_sealant_material,
    decommission_backfill_material as decommission_backfill_material,
    comments as comments,
    ems as ems,
    registries_person.surname as person_responsible,
    registries_organization.name as company_of_person_responsible,
    aquifer_id as aquifer_id,
    aquifer_vulnerability_index as avi,
    storativity as storativity,
    transmissivity as transmissivity,
    hydraulic_conductivity as hydraulic_conductivity,
    specific_storage as specific_storage,
    specific_yield as specific_yield,
    testing_method as testing_method,
    testing_duration as testing_duration,
    analytic_solution_type as analytic_solution_type,
    boundary_effect_code as boundary_effect_code,
    aquifer_lithology_code as aquifer_lithology_code,
    artesian_pressure_head as artesian_pressure_head,
    artesian_conditions as artesian_conditions
    from well
    left join well_subclass_code as wsc on wsc.well_subclass_guid = well.well_subclass_guid
    left join registries_person on
    registries_person.person_guid = well.person_responsible_guid
    left join registries_organization on
    registries_organization.org_guid = well.org_of_person_responsible_guid
    left join (select well_tag_number, count(*) as cur_licences from well
    join well_licences on
    well.well_tag_number = well_licences.well_id
    group by well_tag_number) as licence_q
    on well.well_tag_number = licence_q.well_tag_number
    where well.well_publication_status_code = 'Published' or well.well_publication_status_code = null
    order by well_tag_number;"""

"""
Well V2
"""
CREATE_EXPORT_WELL_VIEW_SQL_V2 = """
drop view if exists export_well_v2_view;
create view export_well_v2_view as 
select 
    well.well_tag_number as well_tag_number, 
    identification_plate_number as identification_plate_number,
    well_identification_plate_attached as well_identification_plate_attached,
    well_status_code as well_status_code, 
    well.well_class_code as well_class_code,
    wsc.well_subclass_code as well_subclass,
    CASE WHEN licence_q.cur_licences > 0 THEN 'LICENSED' ELSE 'UNLICENSED' END as licenced_status_code,
    intended_water_use_code as intended_water_use_code,
    observation_well_number as observation_well_number, 
    obs_well_status_code as obs_well_status_code, 
    water_supply_system_name as water_supply_system_name,
    water_supply_system_well_name as water_supply_system_well_name,
    well.street_address as street_address, 
    well.city as city, 
    legal_lot as legal_lot, 
    legal_plan as legal_plan, 
    legal_district_lot as legal_district_lot, 
    legal_block as legal_block,
    legal_section as legal_section, 
    legal_township as legal_township, 
    legal_range as legal_range,
    land_district_code as land_district_code,
    legal_pid as legal_pid,
    well_location_description as well_location_description,
    st_y(well.geom) as "latitude_Decdeg", 
    st_x(well.geom) as "longitude_Decdeg", 
    utm_zone_code as utm_zone_code, 
    utm_northing as utm_northing, 
    utm_easting as utm_easting,
    coordinate_acquisition_code as coordinate_acquisition_code, 
    bcgs_id as bcgs_id,
    construction_start_date as construction_start_date, 
    construction_end_date as construction_end_date, 
    alteration_start_date as alteration_start_date,
    alteration_end_date as alteration_end_date, 
    decommission_start_date as decommission_start_date, 
    decommission_end_date as decommission_end_date,
    driller_name as driller_name, 
    consultant_name as consultant_name, 
    consultant_company as consultant_company,
    diameter as "diameter_inches", 
    total_depth_drilled as "total_depth_drilled_ft-bgl", 
    finished_well_depth as "finished_well_depth_ft-bgl", 
    final_casing_stick_up as "final_casing_stick_up_inches",
    bedrock_depth as "bedrock_depth_ft-bgl", 
    ground_elevation as "ground_elevation_ft-asl", 
    ground_elevation_method_code as ground_elevation_method_code, 
    static_water_level as "static_water_level_ft-btoc",
    well_yield as "well_yield_Usgpm",
    well_yield_unit_code as well_yield_unit_code,
    artesian_flow as "artesian_flow_Usgpm", 
    artesian_pressure as "artesian_pressure_ft", 
    well_cap_type as well_cap_type, 
    well_disinfected_code as well_disinfected_code,
    well_orientation_code as well_orientation_code,
    alternative_specs_submitted as alternative_specs_submitted,
    surface_seal_material_code as surface_seal_material_code, 
    surface_seal_method_code as surface_seal_method_code,  
    surface_seal_depth as "surface_seal_depth_ft",
    backfill_type as backfill_type,
    backfill_depth as "backfill_depth_ft",
    liner_material_code as liner_material_code, 
    liner_diameter as "liner_diameter_inches", 
    liner_thickness as "liner_thickness_inches", 
    surface_seal_thickness as "surface_seal_thickness_inches",
    liner_from as "liner_from_ft-bgl", 
    liner_to as "liner_to_ft-bgl",
    screen_intake_method_code as screen_intake_method_code, 
    screen_type_code as screen_type_code, 
    screen_material_code as screen_material_code,
    other_screen_material as other_screen_material, 
    screen_information as screen_information,
    screen_opening_code as screen_opening_code, 
    screen_bottom_code as screen_bottom_code, 
    other_screen_bottom as other_screen_bottom,
    filter_pack_from as "filter_pack_from_ft",
    filter_pack_to as "filter_pack_to_ft", 
    filter_pack_material_code as filter_pack_material_code,
    filter_pack_thickness as filter_pack_thickness,
    filter_pack_material_size_code as filter_pack_material_size_code,
    development_hours as development_hours, 
    development_notes as development_notes,
    water_quality_colour as water_quality_colour, 
    water_quality_odour as water_quality_odour,
    yield_estimation_method_code as yield_estimation_method_code,
    yield_estimation_rate as "yield_estimation_rate_USgpm",
    yield_estimation_duration as yield_estimation_duration_hours, 
    static_level_before_test as "static_level_before_test_ft-btoc", 
    drawdown as "drawdown_ft-btoc",
    hydro_fracturing_performed as hydro_fracturing_performed, 
    hydro_fracturing_yield_increase as hydro_fracturing_yield_increase,
    decommission_reason as decommission_reason, 
    decommission_method_code as decommission_method_code, 
    decommission_details as decommission_details, 
    decommission_sealant_material as decommission_sealant_material,
    decommission_backfill_material as decommission_backfill_material,
    comments as comments,
    ems as ems,
    registries_person.surname as person_responsible,
    registries_organization.name as company_of_person_responsible,
    aquifer_id as aquifer_id,
    aquifer_vulnerability_index as "avi_years",
    storativity as storativity,
    transmissivity as transmissivity,
    hydraulic_conductivity as "hydraulic_conductivity_m/s",
    specific_storage as "specific_storage_1/m",
    specific_yield as specific_yield,
    testing_method as testing_method,
    testing_duration as test_duration,
    analytic_solution_type as analytic_solution_type,
    boundary_effect_code as boundary_effect_code,
    aquifer_lithology_code as aquifer_lithology_code,
    artesian_pressure_head as artesian_pressure_head,
    artesian_conditions as artesian_conditions
    from well
    left join well_subclass_code as wsc on wsc.well_subclass_guid = well.well_subclass_guid
    left join registries_person on
    registries_person.person_guid = well.person_responsible_guid
    left join registries_organization on
    registries_organization.org_guid = well.org_of_person_responsible_guid
    left join (select well_tag_number, count(*) as cur_licences from well
    join well_licences on
    well.well_tag_number = well_licences.well_id
    group by well_tag_number) as licence_q
    on well.well_tag_number = licence_q.well_tag_number
    where well.well_publication_status_code = 'Published' or well.well_publication_status_code = null
    order by well_tag_number;"""


class Migration(migrations.Migration):
    """
    JIRA Ticket WATER-1687
        Description:
        This ticket requires us to remove the well.surface_seal_length column.
        In order to achieve this we have to remove this column from version 2 of our view,
            and assign null to it for version 1
        Overall this ticket requires us to remove a column after we've assigned some of the
            data to the surface_seal_depth column, and removed our uses of this column;
            unless shared data such as export or databc, in which case we just keep
            the column but nullify the output (only v1)
        Testing:
        This ticket was tested locally, ensuring that we have some fixture data to work with
    """

    dependencies = [
        ('wells', '0128_merge_20210330_1549'),
    ]

    operations = [
        migrations.RunSQL(CREATE_EXPORT_WELL_VIEW_SQL_V1),
        migrations.RunSQL(CREATE_EXPORT_WELL_VIEW_SQL_V2)
    ]