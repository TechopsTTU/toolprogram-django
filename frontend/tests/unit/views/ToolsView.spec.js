import { shallowMount, mount } from '@vue/test-utils'
import { createStore } from 'vuex'
import ToolsView from '@/views/ToolsView.vue'

// Create a mock store
const createVuexStore = (overrides = {}) => {
  return createStore({
    state: {
      tools: overrides.tools || [],
      loading: overrides.loading || false,
      error: overrides.error || null
    },
    getters: {
      getTools: (state) => state.tools
    },
    actions: {
      fetchTools: jest.fn(),
      deleteTool: jest.fn()
    }
  })
}

describe('ToolsView.vue', () => {
  it('renders loading spinner when loading', () => {
    const store = createVuexStore({ loading: true })
    const wrapper = shallowMount(ToolsView, {
      global: {
        plugins: [store]
      }
    })

    expect(wrapper.find('.spinner-border').exists()).toBe(true)
    expect(wrapper.find('table').exists()).toBe(false)
  })

  it('shows error message when there is an error', () => {
    const errorMessage = 'Failed to load tools'
    const store = createVuexStore({ error: errorMessage })
    const wrapper = shallowMount(ToolsView, {
      global: {
        plugins: [store]
      }
    })

    expect(wrapper.find('.alert-danger').exists()).toBe(true)
    expect(wrapper.find('.alert-danger').text()).toContain(errorMessage)
  })

  it('shows empty state message when there are no tools', () => {
    const store = createVuexStore({ tools: [] })
    const wrapper = shallowMount(ToolsView, {
      global: {
        plugins: [store]
      }
    })

    expect(wrapper.find('.alert-info').exists()).toBe(true)
    expect(wrapper.find('.alert-info').text()).toContain('No tools found')
  })

  it('renders tools table with correct data', () => {
    const mockTools = [
      { id: 1, name: 'Hammer', serial_number: 'H123', calibrated: true, last_checked_in: '2025-06-01T12:00:00Z' },
      { id: 2, name: 'Drill', serial_number: 'D456', calibrated: false, last_checked_in: null }
    ]
    const store = createVuexStore({ tools: mockTools })
    const wrapper = mount(ToolsView, {
      global: {
        plugins: [store],
        stubs: ['router-link']
      }
    })

    // Check if table has correct number of rows (plus header row)
    const rows = wrapper.findAll('tbody tr')
    expect(rows.length).toBe(mockTools.length)

    // Check content of first row
    const firstRow = rows[0]
    expect(firstRow.text()).toContain('Hammer')
    expect(firstRow.text()).toContain('H123')
    expect(firstRow.find('.badge.bg-success').exists()).toBe(true)

    // Check content of second row
    const secondRow = rows[1]
    expect(secondRow.text()).toContain('Drill')
    expect(secondRow.text()).toContain('D456')
    expect(secondRow.find('.badge.bg-warning').exists()).toBe(true)
  })
})
