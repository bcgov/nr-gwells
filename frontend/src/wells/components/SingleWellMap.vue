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
  <div id="single-well-map" class="map">
    <p id="unsupported-browser" v-if="browserUnsupported">Your browser is unable to view the map</p>
  </div>
</template>

<script>
import mapboxgl from 'mapbox-gl'
import GestureHandling from '@geolonia/mbgl-gesture-handling'

import {
  DATABC_ROADS_SOURCE,
  DATABC_CADASTREL_SOURCE,
  DATABC_ROADS_SOURCE_ID,
  DATABC_CADASTREL_SOURCE_ID,
  DATABC_ROADS_LAYER,
  DATABC_CADASTREL_LAYER,
  WELLS_BASE_AND_ARTESIAN_LAYER_ID,
  WELLS_SOURCE_ID,
  WELLS_SOURCE,
  wellsBaseLayer,
  highlightedWellsLayer,
  wellFilterId
} from '../../common/mapbox/layers'
import { setupFeatureTooltips } from '../../common/mapbox/popup'
import { createWellPopupElement } from '../popup'

export default {
  name: 'SingleWellMap',
  props: {
    latitude: {
      type: Number
    },
    longitude: {
      type: Number
    },
    id: {
      type: String
    }
  },
  data () {
    return {
      map: null,
      browserUnsupported: false
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
  methods: {
    initMapBox () {
      if (!mapboxgl.supported()) {
        this.browserUnsupported = true
        return
      }

      var mapConfig = {
        container: this.$el,
        zoom: 6,
        minZoom: 4,
        maxPitch: 0,
        dragRotate: false,
        center: [this.longitude || -126.5, this.latitude || 54.5],
        style: {
          version: 8,
          sources: {
            [DATABC_ROADS_SOURCE_ID]: DATABC_ROADS_SOURCE,
            [DATABC_CADASTREL_SOURCE_ID]: DATABC_CADASTREL_SOURCE,
            [WELLS_SOURCE_ID]: WELLS_SOURCE,
          },
          layers: [
            DATABC_ROADS_LAYER,
            DATABC_CADASTREL_LAYER,
            wellsBaseLayer({ filter: wellFilterId(this.id) }),
            highlightedWellsLayer({ filter: ['!', wellFilterId(this.id)] })
          ]
        }
      }

      this.map = new mapboxgl.Map(mapConfig)
      new GestureHandling({ modifierKey: 'ctrl' }).addTo(this.map)

      /* Add controls */

      this.map.addControl(new mapboxgl.NavigationControl({ showCompass: false }), 'top-left')
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

      /*
      const layers = [{
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
        ],
      }]
      this.legendControl = new LegendControl({
        layers: layers
      })
      this.map.addControl(this.legendControl, 'bottom-right')
      */

      this.map.on('load', () => {
        if (this.longitude && this.latitude) {
          // buildLeafletStyleMarker(this.longitude, this.latitude).addTo(this.map)

          this.map.setZoom(12)
        }

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

        this.$emit('mapLoaded')
      })
    }
  }
}
</script>
<style lang="scss">
@import "~mapbox-gl/dist/mapbox-gl.css";

#single-well-map {
  height: 500px;
}
</style>
