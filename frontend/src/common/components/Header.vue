<template>
  <header id="header">
    <b-navbar type="dark" class="navbar-expand-lg d-print-block" bg-variant="primary" toggleable="md">
      <!-- Navbar content -->
      <b-container>
        <a class="navbar-brand" href="https://www2.gov.bc.ca">
          <img
              class="nav-logo img-fluid d-none d-sm-block"
              src="@/common/assets/images/17_gov3_bc_logo.svg"
              width="152" height="55"
              alt="B.C. Government Logo">
          <img
              class="img-fluid d-none d-sm-block nav-logo-print"
              src="@/common/assets/images/17_gov3_bc_logo_transparent.svg"
              width="152" height="55"
              alt="B.C. Government Logo">
          <img
              class="nav-logo img-fluid d-sm-none"
              src="@/common/assets/images/01_gov3_bc_symbol.svg"
              width="61"
              height="43"
              alt="B.C. Government Logo">
        </a>
        <b-navbar-nav>
          <li class="bc-nav-title d-none d-md-block">Groundwater Wells and Aquifers{{getEnvironmentMessage}}</li>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <li>
            <keycloak-auth class="d-none d-sm-block d-print-none" v-if="auth !== 'hide'" id="keycloak-auth"/>
          </li>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto d-sm-none">
          <b-navbar-toggle class="d-sm-none" target="nav_collapse"/>
        </b-navbar-nav>
      </b-container>
    </b-navbar>
    <b-navbar class="bc-nav-links py-0" toggleable="sm" type="dark">
      <b-container>
        <b-collapse class="py-2" is-nav id="nav_collapse">
          <b-nav-text class="d-sm-none text-light">Groundwater Wells and Aquifers</b-nav-text>
          <b-navbar-nav class="gwells-nav">
            <b-nav-item id="ribbon-search" class="navbar-link lvl2-link" :to="{ name: 'wells-home'}">Well Search</b-nav-item>
            <b-nav-item id="ribbon-aquifers" v-if="show.aquifers" class="navbar-link lvl2-link" :to="{ name: 'aquifers-home' }">Aquifer Search</b-nav-item>
            <b-nav-item id="ribbon-crosssection" v-if="show.bulk" class="navbar-link lvl2-link" :to="{ name: 'CrossHome' }">Cross Section</b-nav-item>
            <b-nav-item id="ribbon-registry" class="navbar-link lvl2-link" :to="{ name: 'SearchHome'}">Registry Search</b-nav-item>
            <b-nav-item class="navbar-link lvl2-link" v-if="show.dataEntry" :to="{ name: 'SubmissionsHome'}">Submit Report</b-nav-item>
            <b-nav-item id="ribbon-bulk" class="navbar-link lvl2-link" v-if="show.bulk" :to="{ name: 'bulk-home' }">Bulk Upload</b-nav-item>
            <b-nav-item id="ribbon-qaqc" class="navbar-link lvl2-link" v-if="show.qaqc" :to="{ name: 'qaqc' }">QA/QC Dashboard</b-nav-item>
            <b-nav-item id="ribbon-surveys" class="navbar-link lvl2-link" v-if="show.surveys" :to="{ name: 'Surveys' }">Admin</b-nav-item>
            <b-nav-item id="ribbon-groundwaterinfo" class="navbar-link lvl2-link" :to="{ name: 'groundwater-information' }">Groundwater Information</b-nav-item>
            <b-nav-item class="d-sm-none"><keycloak-auth v-if="auth !== 'hide'" id="keycloak-auth-xs"/></b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </header>
</template>

<script>
import { mapGetters } from 'vuex'
import Auth from '@/common/components/Auth.vue'
export default {
  components: {
    'keycloak-auth': Auth
  },
  props: ['auth'],
  data () {
    return {}
  },
  computed: {
    ...mapGetters(['userRoles', 'config']),
    hasConfig () {
      return Boolean(this.config)
    },
    getEnvironmentMessage () {
      /**
       * return a message based on the current url location,
       * if gwells-staging or testapps.nrs.gov.bc.ca in url then return ' - STAGING' otherwise ''
       */
      return (window.location.href.indexOf('gwells-staging') > -1 ||
        window.location.href.indexOf('testapps.nrs.gov.bc.ca') > -1) ? ' - STAGING' : ''
    },
    show () {
      const adminMeta = document.head.querySelector('meta[name="show.admin"]')
      let bulk = false
      if (this.userRoles.bulk) {
        bulk = Object.values(this.userRoles.bulk).some(x => x)
      }
      return {
        dataEntry: this.hasConfig && this.userRoles.submissions.edit === true,
        admin: adminMeta ? adminMeta.content === 'true' : false,
        aquifers: this.hasConfig && this.config.enable_aquifers_search === true,
        surveys: this.hasConfig && this.userRoles.surveys.edit === true,
        qaqc: this.hasConfig && this.userRoles.idir === true && this.userRoles.submissions.edit === true,
        bulk
      }
    }
  }
}
</script>

<style lang="scss">
@import '~bootstrap/scss/_functions';
@import '~bootstrap/scss/_variables';
@import '~bootstrap/scss/mixins/_breakpoints';

.navbar {
  margin-bottom: 0px;
}
.nav-item {
  font-size: 13px;
}
.bc-nav-title {
  font-size: 2em;
  color: #fff!important;
  margin-bottom: -10px;
}
.bc-nav-links {
  background-color: #38598a;
  border-bottom: 0px;
  padding-top: 0px;
  padding-bottom: 0px;
  -webkit-box-shadow: 0px 3px 3px 1px rgba(51, 51, 51, 0.5);
  -moz-box-shadow: 0px 3px 3px 1px rgba(51, 51, 51, 0.5);
  box-shadow: 0px 3px 3px 1px rgba(51, 51, 51, 0.5);
}
header li + li {
  @include media-breakpoint-up(sm) {
    border-left: 1px solid #607D8B;
  }
}
.lvl2-link a {
  padding-top:0;
  padding-bottom:0;
}
.nav-logo-print {
  height: 0px !important;
}
@media print {
  header nav {
    background-color: rgba(0,0,0,0) !important;
    border-bottom: none !important;
  }
  .bc-nav-title {
    color: #000 !important;
  }
  .nav-logo-print {
    height: 55px !important;
  }
  .nav-logo {
    height: 0px !important;
  }
}
</style>
