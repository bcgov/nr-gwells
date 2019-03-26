"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import reversion
import zipfile
import tempfile
import os

from django.utils import timezone
from django.contrib.gis.db import models
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry

from gwells.models import AuditModel
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinValueValidator, MaxValueValidator
from reversion.models import Version


class WaterRightsPurpose(AuditModel):
    """
    Material choices for describing Aquifer Material
    """
    code = models.CharField(primary_key=True, max_length=10,
                            db_column='water_rights_purpose_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(default=0)

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'water_rights_purpose_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Water Rights Purpose Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class WaterRightsLicence(AuditModel):
    """
    Material choices for describing Aquifer Material
    """

    aquifer_licence_id = models.AutoField(
        primary_key=True, verbose_name="Aquifer ID Number")

    purpose = models.ForeignKey(
        WaterRightsPurpose,
        db_column='water_rights_purpose_code',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Water Rights Purpose Reference",
        related_name='licences')

    licence_number = models.BigIntegerField(db_index=True)
    quantity = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True, verbose_name='Quanitity')

    well = models.ForeignKey(
        'wells.Well',
        related_name='licences',
        on_delete=models.CASCADE
    )

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Aquifer Licences'

    def __str__(self):
        return '{} - {}'.format(self.well, self.licence_number)


class AquiferMaterial(AuditModel):
    """
    Material choices for describing Aquifer Material
    """
    code = models.CharField(primary_key=True, max_length=10,
                            db_column='aquifer_material_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'aquifer_material_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Aquifer Material Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class AquiferSubtype(AuditModel):
    """
    Subtypes of Aquifer
    """
    code = models.CharField(primary_key=True, max_length=3,
                            db_column='aquifer_subtype_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'aquifer_subtype_code'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class AquiferProductivity(AuditModel):
    """
    Productivity choices for describing Aquifer
    -------------------
    """
    code = models.CharField(primary_key=True, max_length=1,
                            db_column='aquifer_productivity_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'aquifer_productivity_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Aquifer Productivity Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class AquiferDemand(AuditModel):
    """
    Demand choices for describing Aquifer
    """
    code = models.CharField(primary_key=True, max_length=1,
                            db_column='aquifer_demand_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'aquifer_demand_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Aquifer Demand Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class WaterUse(AuditModel):
    """
    Type of Known Water Use choices for describing Aquifer
    -------------------
    """
    code = models.CharField(
        primary_key=True, max_length=2, db_column='water_use_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'water_use_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Aquifer Water Use Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class QualityConcern(AuditModel):
    code = models.CharField(primary_key=True, max_length=2,
                            db_column='quality_concern_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'quality_concern_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Aquifer Quality Concern Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


class AquiferVulnerabilityCode(AuditModel):
    """
    Demand choices for describing Aquifer
    """
    code = models.CharField(primary_key=True, max_length=1,
                            db_column='aquifer_vulnerability_code')
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)

    class Meta:
        db_table = 'aquifer_vulnerability_code'
        ordering = ['display_order', 'code']
        verbose_name_plural = 'Aquifer Vulnerability Codes'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)


@reversion.register()
class Aquifer(AuditModel):
    """
    An underground layer of water-bearing permeable rock, rock fractures or unconsolidated materials
    (gravel, sand, or silt), from which groundwater is extracted using a water well.

    This table holds ONLY the aquifers to which we have associated one or more wells.  It is not
    the definitive source of all aquifers in the province.
    """
    aquifer_id = models.AutoField(
        primary_key=True, verbose_name="Aquifer ID Number")
    aquifer_name = models.CharField(max_length=100, blank=True, null=True)
    location_description = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Description of Location')
    material = models.ForeignKey(
        AquiferMaterial,
        db_column='aquifer_material_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Material Reference",
        related_name='aquifers')
    subtype = models.ForeignKey(
        AquiferSubtype,
        db_column='aquifer_subtype_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Subtype Reference",
        related_name='aquifers')
    area = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True, verbose_name='Size (square km)')
    vulnerability = models.ForeignKey(
        AquiferVulnerabilityCode,
        # TODO: Spelling mistake below!
        db_column='aquifer_vulnerablity_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Aquifer Vulnerabiliy")
    productivity = models.ForeignKey(
        AquiferProductivity,
        db_column='aquifer_productivity_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Productivity Reference",
        related_name='aquifers')
    demand = models.ForeignKey(
        AquiferDemand,
        db_column='aquifer_demand_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Demand Reference",
        related_name='aquifers')
    known_water_use = models.ForeignKey(
        WaterUse,
        db_column='water_use_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Known Water Use Reference",
        related_name='aquifers')
    quality_concern = models.ForeignKey(
        QualityConcern,
        db_column='quality_concern_code',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Quality Concern Reference",
        related_name='aquifers')
    litho_stratographic_unit = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Lithographic Stratographic Unit')
    mapping_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(timezone.now().year)],
        blank=True,
        null=True,
        verbose_name="Date of Mapping",
        help_text="Use the following format: <YYYY>")
    notes = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name='Notes on Aquifer, for internal use only.')

    #shapefile = models.FileField(blank=True, default='')
    geom = models.PolygonField(srid=3005, null=True)

    history = GenericRelation(Version)

    def load_shapefile(self, f):

        zip_ref = zipfile.ZipFile(f)

        output_dir = tempfile.mkdtemp()
        for item in zip_ref.namelist():
            # Check filename endswith shp
            zip_ref.extract(item, output_dir)
            if item.endswith('.shp'):
                # Extract a single file from zip
                the_shapefile = os.path.join(output_dir, item)
                # break
        zip_ref.close()

        ds = DataSource(the_shapefile)
        for layer in ds:
            for feat in layer:
                geom = feat.geom
                # Make a GEOSGeometry object using the string representation.
                wkt = geom.wkt
                if not geom.srid == 3005:
                    raise Exception("Only BC Albers data is accepted.")
                geos_geom = GEOSGeometry(wkt, srid=3005)
                # Just return the first feature in the shapefile.
                # TODO: should we have validation that the shapefile just contains one
                # POLYGON feature?
                self.geom = geos_geom
                return geos_geom
        raise Exception('no feature found.')
        # TODO: cleanup temporary files

    class Meta:
        db_table = 'aquifer'
        ordering = ['aquifer_id']
        verbose_name_plural = 'Aquifers'

    def __str__(self):
        return '{} - {}'.format(self.aquifer_id, self.aquifer_name)


class AquiferResourceSection(AuditModel):
    """
    Defines the available sections (categories) of aquifer resources.
    """
    code = models.CharField(primary_key=True, max_length=1,
                            db_column='aquifer_resource_section_code')
    name = models.CharField(max_length=100)
    effective_date = models.DateTimeField(default=timezone.now, null=False)
    expiry_date = models.DateTimeField(default=timezone.make_aware(
        timezone.datetime.max, timezone.get_default_timezone()), null=False)
    description = models.CharField(max_length=100, default="")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Aquifer Resource Sections'
        db_table = 'aquifer_resource_section_code'

    def __str__(self):
        return '{} - {}'.format(self.code, self.description)

    def __str__(self):
        return self.name


class AquiferResource(AuditModel):
    """
    A PDF document associated with a given aquifer.
    """
    id = models.AutoField(
        primary_key=True,
        verbose_name="Aquifer Resource Identifier",
        db_column='aquifer_resource_id')
    aquifer = models.ForeignKey(
        Aquifer,
        related_name='resources',
        on_delete=models.CASCADE)
    section = models.ForeignKey(
        AquiferResourceSection,
        db_column='aquifer_resource_section_code',
        verbose_name="Aquifer Resource Section",
        on_delete=models.CASCADE,
        help_text="The section (category) of this resource.")
    name = models.CharField(
        max_length=255,
        verbose_name="Aquifer Resource Name",
        help_text="",
    )
    url = models.URLField(
        verbose_name="PDF Document URL",
        max_length=255,
        help_text="A resolvable link to the PDF document associated with this aquifer resource.")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Aquifer Resource'

    def __str__(self):
        return self.name
