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
  <b-card class="container p-1">
      <h1 class="card-title" id="CrossSectionTitle">Cross Section Home</h1>
      <div>
        <div>
          <MapLoadingSpinner :loading="loadingMap"/>
          <CrossMap
            :focusedWells="focusedWells"
          />
        </div>
      </div>
    </b-card>
</template>

<script>
import MapLoadingSpinner from '../../common/components/MapLoadingSpinner.vue'
import CrossMap from '../components/CrossMap.vue'

export default {
  name: 'CrossHome',
  components: {
    CrossMap,
    MapLoadingSpinner
  },
  data () {
    return {
      scrolled: false,
      loadingMap: false,
      focusedWells: [],
      mapServerErrorMessage: null,
      showMapErrorMessage: false,
    }
  },
  methods: {
    handleScroll () {
      this.scrolled = window.scrollY > 100
    },
    handleMapError (err) {
      if (err.noFeatures) {
        this.noWellsInView = true
      } else if (err.serverError) {
        this.mapServerErrorMessage = err.serverError
      }
    }
  },
  watch: {
    beforeMount () {
      this.loadingMap = true
      this.scrolled = window.scrollY > 100
      window.addEventListener('scroll', this.handleScroll)
    },
    beforeDestroy () {
      window.removeEventListener('scroll', this.handleScroll)
    }
  }
}
</script>

<!--
components: {
  InfoPanel,
  Map,
  WelcomeMessage
},
data: () => ({
  sidebarColumnDefaults: {
    cols: 12,
    md: 6,
    lg: 4,
    xl: 3
  }
}),
computed: {
  sidebarColumns () {
    const sidebarColumns = this.$route.meta.sidebarColumns || {}
    return Object.assign(this.sidebarColumnDefaults, sidebarColumns)
  },
  mapColumns () {
    if (this.$route.meta.hide) {
      return {
        cols: 12,
        md: 12,
        lg: 12,
        xl: 12
      }
    }
    return {
      cols: 12 - this.sidebarColumns.cols,
      md: 12 - this.sidebarColumns.md,
      lg: 12 - this.sidebarColumns.lg,
      xl: 12 - this.sidebarColumns.xl
    }
  },
  ...mapGetters('map', ['map'])
}
} -->

<style>
</style>
