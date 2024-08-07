<template>
  <b-container class="p-1 p-md-3">
    <b-card no-body class="mb-3">
      <b-breadcrumb :items="breadcrumbs" class="py-0 my-2"></b-breadcrumb>
    </b-card>
    <b-card title="Manage Companies">

      <!-- Company selector (used to select company to edit) -->
      <b-row>
        <b-col cols="12" md="7">
          <b-form-group label="Select a company:" label-for="orgEditSelectDropdown">
            <v-select
                id="orgEditSelectDropdown"
                :options="companies"
                label="org_verbose_name"
                v-model="selectedCompany"
                placeholder="Begin typing a company name"
                ></v-select>
          </b-form-group>
        </b-col>
        <b-col cols="12" md="5">
          <b-alert variant="warning" :show="!!companyListError" dismissible @dismissed="companyListError=false">
            Error retrieving list of companies. Please try again later.
          </b-alert>
        </b-col>
      </b-row>

      <!-- Add company button (opens 'add company' modal) and success feedback -->
      <b-row>
        <b-col>
          <b-button
              id="orgAddNewButton"
              type="button"
              v-b-modal.orgAddModal
              variant="primary"
              size="sm"
              class="mb-5">
            <i class="fa fa-plus-square-o"></i> Add new company</b-button>
          <organization-add @newOrgAdded="newOrgHandler"></organization-add>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-alert variant="success" id="orgAddSuccessAlert" :show="companyAddSuccess" dismissible @dismissed="companyAddSuccess=false">Company added.</b-alert>
        </b-col>
      </b-row>

      <!-- Selected company details and edit form fields -->
      <b-card no-body class="p-2 p-md-3" v-if="!!selectedCompany">
        <h6 class="card-subtitle mb-3">Company Information</h6>
        <b-form @submit.prevent="submitConfirm" @reset.prevent="cancelConfirm">
          <b-row>
            <b-col cols="12" md="5">
                <b-form-group
                  label="Company name:"
                  label-for="orgEditNameInput">
                  <b-form-input
                    :disabled="!selectedCompany"
                    id="orgEditNameInput"
                    type="text"
                    v-model="companyForm.name"/>
                </b-form-group>
            </b-col>
              <b-col cols="12" md="5" offset-md="1">
                <b-form-group
                  label="Street address:"
                  label-for="orgEditAddressInput">
                  <b-form-input
                    :disabled="!selectedCompany"
                    id="orgEditAddressInput"
                    type="text"
                    v-model="companyForm.street_address"/>
                </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col cols="12" md="5">
                <b-form-group
                  label="City:"
                  label-for="orgEditCityInput">
                  <b-form-input
                    :disabled="!selectedCompany"
                    id="orgEditCityInput"
                    type="text"
                    v-model="companyForm.city"/>
                </b-form-group>
            </b-col>
              <b-col cols="12" md="5" offset-md="1">
                <b-form-group
                  label="Province:"
                  label-for="orgEditProvinceInput">
                  <b-form-select
                    :disabled="!selectedCompany"
                    id="orgEditProvinceInput"
                    :state="validation.province_state"
                    :options="provinceStateOptions"
                    aria-describedby="provInputFeedback"
                    v-model="companyForm.province_state">
                  </b-form-select>
                  <b-form-invalid-feedback id="provInputFeedback">
                    <div v-for="(error, index) in fieldErrors.province_state" :key="`provInput error ${index}`">
                      {{ error }}
                    </div>
                  </b-form-invalid-feedback>
                </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col cols="12" md="5">
                <b-form-group
                  label="Postal code:"
                  label-for="orgEditPostalInput">
                  <b-form-input
                    :disabled="!selectedCompany"
                    id="orgEditPostalInput"
                    type="text"
                    v-model="companyForm.postal_code"/>
                </b-form-group>
            </b-col>
          </b-row>
          <b-row class="mt-4">
            <b-col cols="12" md="5">
              <b-form-group
                label="Office telephone number:"
                label-for="orgEditPhoneInput">
                <b-form-input
                  :disabled="!selectedCompany"
                  id="orgEditPhoneInput"
                  type="text"
                  :formatter="formatTel"
                  lazy-formatter
                  v-model="companyForm.main_tel"/>
              </b-form-group>
            </b-col>
            <b-col cols="12" md="5" offset-md="1">
                <b-form-group
                  label="Fax number:"
                  label-for="orgEditFaxInput">
                  <b-form-input
                    :disabled="!selectedCompany"
                    id="orgEditFaxInput"
                    type="text"
                    :formatter="formatTel"
                    lazy-formatter
                    v-model="companyForm.fax_tel"/>
                </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col cols="12" md="5">
              <b-form-group
                label="Email:"
                label-for="orgEditEmailInput">
                <b-form-input
                    id="orgEditEmailInput"
                    type="text"
                    :state="validation.email"
                    :disabled="!selectedCompany"
                    aria-describedby="orgEditEmailFeedback"
                    v-model="companyForm.email"/>
                <b-form-invalid-feedback id="orgEditEmailFeedback">
                  <div v-for="(error, index) in fieldErrors.email" :key="`urlInput error ${index}`">
                    {{ error }}
                  </div>
                </b-form-invalid-feedback>
              </b-form-group>
            </b-col>
            <b-col cols="12" md="5" offset-md="1">
              <b-form-group
                label="Website:"
                label-for="orgEditWebsiteInput">
                <b-form-input
                  :disabled="!selectedCompany"
                  id="orgEditWebsiteInput"
                  :state="validation.website_url"
                  aria-describedby="orgEditWebsiteFeedback"
                  placeholder="eg. http://www.example.com"
                  type="text"
                  v-model="companyForm.website_url"/>
                <b-form-invalid-feedback id="orgEditWebsiteFeedback">
                    <div v-for="(error, index) in fieldErrors.website_url" :key="`websiteInput error ${index}`">
                      {{ error }}
                    </div>
                </b-form-invalid-feedback>
                <b-form-text id="orgEditEmailInput">
                  Use a full website address, including http://
                </b-form-text>
              </b-form-group>
            </b-col>
            <b-col cols="12" md="12">
              <b-form-group label="Region:" label-for="regionOptions">
                <b-form-select
                    multiple="multiple"
                    id="regionOptions"
                    v-model="companyForm.regional_areas"
                    class="mb-3">
                    <option v-for="region in regionOptions" :key="`${region.regional_area_guid}`" :value="region.regional_area_guid">{{ region.name }}</option>
                </b-form-select>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row class="mt-3">
            <b-col>
              <button type="submit" class="btn btn-primary" ref="orgUpdateSaveBtn" :disabled="!selectedCompany || !formChanged">Update</button>
              <button type="reset" class="btn btn-light" ref="orgUpdateCancelBtn" :disabled="!selectedCompany || !formChanged">Cancel</button>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-alert class="mt-3" variant="success" id="orgUpdateSuccessAlert" :show="companyUpdateSuccess" dismissible @dismissed="companyUpdateSuccess=false">
                Successfully updated company information.
              </b-alert>
            </b-col>
          </b-row>

          <!-- Modals for confirming update/cancel editing -->
          <b-modal
              id="orgUpdateModal"
              v-model="confirmSubmitModal"
              centered
              title="Confirm update"
              @shown="focusSubmitModal"
              :return-focus="$refs.orgUpdateSaveBtn">
            Are you sure you want to save these changes?
            <div slot="modal-footer">
              <b-btn variant="primary" @click="confirmSubmitModal=false;submitForm()" ref="confirmSubmitConfirmBtn">
                Save
              </b-btn>
              <b-btn variant="light" @click="confirmSubmitModal=false">
                Cancel
              </b-btn>
            </div>
          </b-modal>
          <b-modal
              v-model="confirmCancelModal"
              centered
              title="Confirm cancel"
              @shown="focusCancelModal"
              :return-focus="$refs.orgUpdateCancelBtn">
            Are you sure you want to discard your changes?
            <div slot="modal-footer">
              <b-btn variant="secondary" @click="confirmCancelModal=false" ref="cancelSubmitCancelBtn">
                Cancel
              </b-btn>
              <b-btn variant="danger" @click="confirmCancelModal=false;formReset()">
                Discard
              </b-btn>
            </div>
          </b-modal>
        </b-form>
      </b-card>

      <!-- Company notes -->
      <notes
          class="mt-3"
          v-if="!!companyDetails"
          type="organization"
          @updated="loadCompanyDetails()"
          :guid="companyDetails.org_guid"
          :record="companyDetails"></notes>

      <!-- Change history for this record -->
      <change-history
          ref="changeHistory"
          class="my-3"
          v-if="!!selectedCompany"
          resource="organization"
          :id="selectedCompany.org_guid"></change-history>

      <!-- Delete company button and confirmation modals -->
      <div v-if="!!companyDetails">
        <p class="mt-3">
          There {{ companyDetails.registrations_count === 1 ? 'is': 'are' }}
          <span class="font-weight-bold">{{ companyDetails.registrations_count }}</span>
          {{ companyDetails.registrations_count === 1 ? 'registrant': 'registrants' }}
          listed under
          {{ selectedCompany.name }}{{ selectedCompany.name.slice(-1) === '.' ? '' : '.' }}
        </p>
        <b-table
          v-if="companyRegistrants.length > 0"
          id="registrants"
          striped
          hover
          small
          :items="companyRegistrants"
          :fields="['name', 'contact_tel', 'contact_email']"
        >
          <template v-slot:cell(name)="row">
            <router-link :to="{ name: 'PersonDetail', params: { person_guid: row.item.person_guid }}">{{ row.item.surname }}, {{ row.item.first_name }}</router-link>
          </template>
        </b-table>
        <b-button
          variant="danger"
          :disabled="companyDetails.registrations_count > 0"
          @click="companyDeleteConfirm()"
        >
          Delete this company
        </b-button>
        <p v-if="companyDetails.registrations_count > 0" class="delete-company">You must remove all registrants from this company before deleting.</p>
      </div>
      <b-modal
          id="orgDeleteModal"
          v-model="companyDeleteModal"
          centered
          title="Confirm delete"
          @shown="focusDeleteModal"
          :return-focus="$refs.orgDeleteBtn">
        Are you sure you want to delete this company?
        <div slot="modal-footer">
          <b-btn variant="secondary" @click="companyDeleteModal=false" ref="companyDeleteCancelBtn">
            Cancel
          </b-btn>
          <b-btn variant="danger" @click="companyDeleteModal=false;companyDelete()">
            Delete
          </b-btn>
        </div>
      </b-modal>
      <b-alert variant="success" class="mt-3" id="orgDeleteSuccessAlert" :show="!!companyDeleted" dismissible @dismissed="companyDeleted=false">
          {{ companyDeleted }} removed.
      </b-alert>
    </b-card>
  </b-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ApiService from '@/common/services/ApiService.js'
import OrganizationAdd from '@/registry/components/people/OrganizationAdd.vue'
import Notes from '@/registry/components/people/Notes.vue'
import ChangeHistory from '@/common/components/ChangeHistory.vue'
import inputFormatMixin from '@/common/inputFormatMixin.js'
import { FETCH_DRILLER_OPTIONS } from '@/registry/store/actions.types'

export default {
  name: 'OrganizationEdit',
  components: {
    OrganizationAdd,
    Notes,
    ChangeHistory
  },
  mixins: [inputFormatMixin],
  data () {
    return {
      breadcrumbs: [
        {
          text: 'Registry',
          to: { name: 'SearchHome' }
        },
        {
          text: 'Manage Companies',
          active: true
        }
      ],

      // companies list from API
      companies: [{ name: '', org_guid: '', org_verbose_name: '' }],
      selectedCompany: null,

      // company details from API (loaded after selecting a company)
      companyDetails: null,
      companyRegistrants: [],
      // company form fields
      companyForm: {
        name: '',
        street_address: '',
        city: '',
        province_state: null,
        postal_code: '',
        email: '',
        main_tel: '',
        fax_tel: '',
        website_url: '',
        regional_areas: []
      },
      companyNotesForm: '',

      // add/update company success messages
      companyAddSuccess: false,
      companyUpdateSuccess: false,
      companyListError: false,
      companyDeleted: false,
      companyDeleteError: false,
      fieldErrors: {},

      // confirm popups
      confirmSubmitModal: false,
      confirmCancelModal: false,
      companyDeleteModal: false
    }
  },
  computed: {
    validation () {
      return {
        website_url: (this.fieldErrors.website_url && this.fieldErrors.website_url.length) ? false : null,
        province_state: (this.fieldErrors.province_state && this.fieldErrors.province_state.length) ? false : null,
        email: (this.fieldErrors.email && this.fieldErrors.email.length) ? false : null
      }
    },
    fieldsChanged () {
      // check if any of the company detail input fields changed (to toggle update/cancel buttons)
      // returns an object containing each field, and true/false if value changed or not

      const fields = {}
      if (this.selectedCompany) {
        Object.keys(this.companyForm).forEach((key) => {
          // sets a field as true if it has changed
          // need to convert empty strings to null to compare to null/blank values from API
          fields[key] = ((this.companyForm[key] ? this.companyForm[key] : null) !== this.selectedCompany[key])
        })
      }
      return fields
    },
    formChanged () {
      // returns true or false if any of the fields changed. Uses fieldsChanged() method above
      return (Object.keys(this.fieldsChanged).map(x => this.fieldsChanged[x]).includes(true))
    },
    ...mapGetters('registriesStore', ['provinceStateOptions', 'regionOptions'])
  },
  watch: {
    selectedCompany (val) {
      // reset form whenever selectedCompany (dropdown) changes
      this.formReset()

      // fetch extra company data
      this.companyDetails = null
      if (val) {
        this.loadCompanyDetails()
      }
    }
  },
  methods: {
    newOrgHandler (orgGuid) {
      // called when a new company created
      // shows a success message and sets currently selected company to the new one
      this.companyUpdateSuccess = false
      this.companyAddSuccess = true
      this.loadCompanies().then(() => {
        this.selectedCompany = this.companies.find((company) => company.org_guid === orgGuid)
        this.companyAddSuccess = true
      })
    },
    submitConfirm () {
      // popup confirmation for form submit
      // also clear 'company add' success message if it is still active
      this.companyAddSuccess = false
      this.companyUpdateSuccess = false
      this.confirmSubmitModal = true
    },
    submitForm () {
      // submits a PATCH request to API with the updated company details

      const data = {}

      // remove null & empty string values, and the guid (not needed in data object)
      Object.keys(this.companyForm).forEach((key) => {
        if (key !== 'org_guid') {
          data[key] = this.companyForm[key]
        }
      })
      ApiService.patch('organizations', this.selectedCompany.org_guid, data).then((response) => {
        // after successful request, load the company list again
        this.loadCompanies().then((response) => {
          this.selectedCompany = this.companies.find((company) => company.org_guid === this.selectedCompany.org_guid)
          this.companyUpdateSuccess = true
          this.resetFieldErrors()
        })
      }).catch((error) => {
        // if any field errors are returned by the API (e.g. website_url: ['Enter a valid address']), store them
        this.fieldErrors = error.response.data
      })
    },
    cancelConfirm () {
      // also clear 'company add' success message if it is still active
      this.companyAddSuccess = false
      this.companyUpdateSuccess = false
      this.confirmCancelModal = true
    },
    focusSubmitModal () {
      // focus the "submit" button in the confirm save note popup
      this.$refs.confirmSubmitConfirmBtn.focus()
    },
    focusCancelModal () {
      // focus the "cancel" button in the confirm discard popup
      this.$refs.cancelSubmitCancelBtn.focus()
    },
    focusDeleteModal () {
      this.$refs.companyDeleteCancelBtn.focus()
    },
    formReset () {
      // reset all company edit form fields (with default values)
      const company = this.selectedCompany || {}
      this.companyForm.name = company.name || ''
      this.companyForm.street_address = company.street_address || ''
      this.companyForm.city = company.city || ''
      this.companyForm.province_state = company.province_state || null
      this.companyForm.postal_code = company.postal_code || ''
      this.companyForm.email = company.email || ''
      this.companyForm.main_tel = company.main_tel || ''
      this.companyForm.fax_tel = company.fax_tel || ''
      this.companyForm.website_url = company.website_url || ''
      this.companyForm.regional_areas = company.regional_areas || []
      this.resetFieldErrors()
    },
    resetFieldErrors () {
      this.fieldErrors = {}
    },
    loadCompanies () {
      // load full list of companies when page loads (for dropdown picker)
      return ApiService.query('organizations').then((response) => {
        this.companies = response.data
      }).catch((e) => {
        this.companyListError = e.response
      })
    },
    loadCompanyDetails () {
      // List of companies only contains basic details. When one is selected, get the full set of details
      // plus all notes for that company
      ApiService.get('organizations', this.selectedCompany.org_guid)
        .then((response) => {
          this.companyRegistrants = [];
          this.companyDetails = response.data
          // Fetch data on Registrants
          ApiService.query(`drillers?search=${encodeURIComponent(this.companyDetails.name)}`)
            .then(({data}) => {
              this.companyRegistrants = data.results;
            });
        }).catch((e) => {
          this.companyListError = e.response.data
        })

      // update changeHistory when company is updated
      if (this.$refs.changeHistory) {
        this.$refs.changeHistory.update()
      }
    },
    companyDeleteConfirm () {
      this.companyDeleteModal = true
    },
    companyDelete () {
      // after confirmation received via popup, clear any success messages and send delete request
      return ApiService.delete('organizations', this.selectedCompany.org_guid).then((response) => {
        this.companyDeleted = this.selectedCompany.name
        this.selectedCompany = null
        this.companyUpdateSuccess = false
        this.companyAddSuccess = false
        this.loadCompanies()
      }).catch((e) => {
        this.companyDeleteError = e.response.data
      })
    },
    ...mapActions('registriesStore', [
      FETCH_DRILLER_OPTIONS
    ])
  },
  created () {
    this.loadCompanies()
    this.FETCH_DRILLER_OPTIONS()
  }
}
</script>

<style>
  .delete-company {
    margin: 0.25em 0;
  }
  button:disabled {
    cursor: not-allowed
  }
</style>
