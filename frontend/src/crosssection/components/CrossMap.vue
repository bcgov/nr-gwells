/*
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
*/
<template>
  <div id="cross-map" class="map"/>
</template>

<script>
import mapboxgl from 'mapbox-gl'
import GestureHandling from '@geolonia/mbgl-gesture-handling'

import {
  DATABC_ROADS_SOURCE,
  DATABC_CADASTREL_SOURCE,
  WELLS_SOURCE_ID,
  DATABC_ROADS_SOURCE_ID,
  DATABC_CADASTREL_SOURCE_ID,
  DATABC_ROADS_LAYER,
  DATABC_CADASTREL_LAYER,
  wellsBaseAndArtesianLayer,
  WELLS_BASE_AND_ARTESIAN_LAYER_ID,
  FOCUSED_WELLS_SOURCE_ID,
  focusedWellsLayer,
  FOCUSED_WELL_IMAGE_ID,
  FOCUSED_WELL_ARTESIAN_IMAGE_ID,
  FOCUSED_WELL_CLOSED_IMAGE_ID,
  wellLayerFilter,
  WELLS_SOURCE
} from '../../common/mapbox/layers'
import { LegendControl } from '../../common/mapbox/controls'
import { createWellPopupElement } from '../../common/mapbox/popup'
import { PulsingWellImage, PulsingArtesianWellImage, PulsingClosedWellImage } from '../../common/mapbox/images'
import { mapGetters } from 'vuex'
import {CENTRE_LNG_LAT_BC, buildWellsGeoJSON } from '../../common/mapbox/geometry'

import wellsAllLegendSrc from '../../common/assets/images/wells-all.svg'
import wellsArtesianLegendSrc from '../../common/assets/images/wells-artesian.svg'
import wellsClosedLegendSrc from '../../common/assets/images/wells-closed.svg'
import { setupFeatureTooltips } from '../../common/mapbox/popup'

const WELL_FEATURE_PROPERTIES_FOR_POPUP = [
  'well_tag_number',
  'identification_plate_number',
  'street_address',
  'is_published'
]
const FOCUSED_WELL_PROPERTIES = WELL_FEATURE_PROPERTIES_FOR_POPUP.concat(['artesian_conditions', 'well_status'])

export default {
  name: 'CrossMap',
  props: [
    'focusedWells'
  ],
  data () {
    return {
      map: null,
      browserUnsupported: false,
      mapLayers: [
        {
          show: true,
          id: WELLS_BASE_AND_ARTESIAN_LAYER_ID,
          label: 'Wells',
          legend: [
            {
              imageSrc: wellsAllLegendSrc,
              label: 'all'
            },
            {
              imageSrc: wellsArtesianLegendSrc,
              label: 'artesian'
            },
            {
              imageSrc: wellsClosedLegendSrc,
              label: 'closed/abandoned'
            }
          ]
        }
      ]
    }
  },
  mounted () {
    this.$emit('mapLoading')

    this.initMapBox()
  },
  destroyed () {
    this.map.remove()
    this.map = null
  },
  computed: {
    ...mapGetters(['userRoles']),
    showUnpublished () {
      return Boolean(this.userRoles.wells.edit)
    }
  },
  methods: {
    initMapBox () {
      if (!mapboxgl.supported()) {
        this.browserUnsupported = true
        return
      }

      var mapConfig = {
        container: this.$el,
        zoom: 4,
        minZoom: 4,
        maxPitch: 0,
        dragRotate: false,
        center: CENTRE_LNG_LAT_BC,
        style: {
          version: 8,
          sources: {
            [DATABC_ROADS_SOURCE_ID]: DATABC_ROADS_SOURCE,
            [DATABC_CADASTREL_SOURCE_ID]: DATABC_CADASTREL_SOURCE,
            [WELLS_SOURCE_ID]: WELLS_SOURCE,
            [FOCUSED_WELLS_SOURCE_ID]: { type: 'geojson', data: buildWellsGeoJSON([]) }
          },
          layers: [
            DATABC_ROADS_LAYER,
            DATABC_CADASTREL_LAYER,
            //should we filter based on user role? this page is already behind keycloak
            // wellsBaseAndArtesianLayer({ filter: wellLayerFilter(this.showUnpublished) }),
            wellsBaseAndArtesianLayer({ filter: wellLayerFilter(this.showUnpublished) }),
            focusedWellsLayer()
          ]
        }
      }

      this.map = new mapboxgl.Map(mapConfig)
      new GestureHandling({ modifierKey: 'ctrl' }).addTo(this.map)

      /* Add controls */

      this.map.addControl(new mapboxgl.NavigationControl({ showCompass: false }), 'top-left')
      this.map.addControl(new mapboxgl.GeolocateControl({
        positionOptions: {
          enableHighAccuracy: true
        }
      }), 'top-left')
      this.map.addControl(new mapboxgl.ScaleControl({
        maxWidth: 80,
        unit: 'imperial'
      }))
      this.map.addControl(new mapboxgl.ScaleControl({
        maxWidth: 80,
        unit: 'metric'
      }))
      this.map.addControl(new mapboxgl.AttributionControl({
        customAttribution: 'MapBox | Government of British Columbia, DataBC, GeoBC '
      }))

      this.legendControl = new LegendControl({
        layers: this.mapLayers
      })
      this.map.addControl(this.legendControl, 'bottom-right')

      this.map.on('load', () => {
        this.map.addImage(FOCUSED_WELL_ARTESIAN_IMAGE_ID, new PulsingArtesianWellImage(this.map), { pixelRatio: 2 })
        this.map.addImage(FOCUSED_WELL_IMAGE_ID, new PulsingWellImage(this.map), { pixelRatio: 2 })
        this.map.addImage(FOCUSED_WELL_CLOSED_IMAGE_ID, new PulsingClosedWellImage(this.map), { pixelRatio: 2 })

        const tooltipLayers = {
          [WELLS_BASE_AND_ARTESIAN_LAYER_ID]: {
            snapToCenter: true,
            createTooltipContent: (features) => createWellPopupElement(
              features,
              this.map,
              this.$router,
              { canInteract: true, openInNewTab: true }
            )
          }
        }
        setupFeatureTooltips(this.map, tooltipLayers)

        this.setFocusedWells(this.focusedWells)

        this.$emit('mapLoaded')
      })
    },
    setFocusedWells (wells) {
      this.map.getSource(FOCUSED_WELLS_SOURCE_ID).setData(buildWellsGeoJSON(wells, FOCUSED_WELL_PROPERTIES))
    },
    createWellPopupElement (features, { canInteract }) {
      return createWellPopupElement(features, this.map, this.$router, {
        canInteract,
        wellLayerIds: [
          WELLS_BASE_AND_ARTESIAN_LAYER_ID
        ]
      })
    }
  },
  watch: {
    userRoles () {
      this.map.setStyle(this.buildMapStyle())
    }
  }
}
</script>
<style lang="scss">
@import "~mapbox-gl/dist/mapbox-gl.css";
@import "~@mapbox/mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css";

#cross-map {
  height: 600px;
}
</style>
