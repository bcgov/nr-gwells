import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import { merge } from 'lodash'
import CrossHome from '../../../../src/crosssection/views/CrossHome.vue'
import auth from '@/common/store/auth.js'

const localVue = createLocalVue()
localVue.use(Vuex)

describe('CrossHome.vue', () => {
  const getters = {
    userRoles: () => ({ wells: { view: true } })
  }

  const component = (options, storeState = {}) => {
    const store = new Vuex.Store({
      getters,
      modules: { auth }
    })
    store.replaceState(merge(store.state, storeState))

    return shallowMount(CrossHome, { store, localVue })
  }

  it('the page renders', () => {
    const wrapper = component()
    expect(wrapper.find('#CrossSectionTitle').text()).toBe('Cross Section Home')
  })
})
