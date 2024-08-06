import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import Header from '@/common/components/Header.vue'

const localVue = createLocalVue()
localVue.use(Vuex)

describe('Header.vue', () => {
  let getters
  let store

  it('the show computed property allows disabling links', () => {
    getters = {
      config: () => ({ enable_aquifers_search: false }),
      userRoles: () => ({ submissions: { edit: true }, surveys: { edit: true } })
    }
    store = new Vuex.Store({ getters })

    const wrapper = shallowMount(Header, {
      store,
      localVue
    })
    expect(wrapper.vm.show.aquifers).toBe(false)
  })
  it('the show computed property allows enabling links', () => {
    getters = {
      config: () => ({ enable_aquifers_search: true }),
      userRoles: () => ({ submissions: { edit: true }, surveys: { edit: true } })
    }
    store = new Vuex.Store({ getters })

    const wrapper = shallowMount(Header, {
      store,
      localVue
    })

    expect(wrapper.vm.show.aquifers).toBe(true)
  })
})
