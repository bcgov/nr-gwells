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
import json
import reversion
from logging import getLogger
from django.contrib.gis.geos import Point
from django.contrib.auth.models import Group, User

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse

from gwells.settings import REST_FRAMEWORK
from wells.models import Well

class ElevationProfileTests(TestCase):
    
    def test_geo_gratis_profile(self):
        """ Test the GeoGratis API integration """
        line = LineString([(0, 0), (1, 1), (2, 2)])
        response = self.client.get(reverse('elevation_profile'))  # Make sure the URL is correct
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains 'profile' in JSON
        data = response.json()
        self.assertIn('profile', data)
        self.assertIsInstance(data['profile'], list)

    def test_postgis_profile(self):
        """ Test fetching elevation profile from the PostGIS database """
        line = LineString([(0, 0), (1, 1), (2, 2)])
        response = self.client.get(reverse('elevation_profile_db'))  # Adjust URL name as needed
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains elevation data
        data = response.json()
        self.assertIn('profile', data)
        self.assertGreater(len(data['profile']), 0)

class ElevationModelTests(TestCase):
    
    def test_create_elevation(self):
        """ Test creating an Elevation entry with a LineString """
        line = LineString([(0, 0), (1, 1), (2, 2)])
        elevation = Elevation.objects.create(
            distance_from_origin=100,
            elevation=200,
            geom=line
        )
        
        # Verify that the elevation was saved
        self.assertEqual(Elevation.objects.count(), 1)
        self.assertEqual(elevation.distance_from_origin, 100)
        self.assertEqual(elevation.elevation, 200)
