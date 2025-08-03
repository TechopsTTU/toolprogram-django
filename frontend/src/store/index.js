import { createStore } from 'vuex'
import axios from 'axios'

// Configure axios with Django CSRF token handling
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default createStore({
  state: {
    tools: [],
    currentTool: null,
    employees: [],
    currentEmployee: null,
    workcenters: [],
    currentWorkCenter: null,
    loading: false,
    error: null
  },
  getters: {
    getTools: state => state.tools,
    getCurrentTool: state => state.currentTool,
    getEmployees: state => state.employees,
    getWorkCenters: state => state.workcenters,
    isLoading: state => state.loading
  },
  mutations: {
    SET_TOOLS(state, tools) {
      state.tools = tools
    },
    SET_CURRENT_TOOL(state, tool) {
      state.currentTool = tool
    },
    ADD_TOOL(state, tool) {
      state.tools.push(tool)
    },
    UPDATE_TOOL(state, updatedTool) {
      const index = state.tools.findIndex(t => t.id === updatedTool.id)
      if (index !== -1) {
        state.tools.splice(index, 1, updatedTool)
      }
    },
    DELETE_TOOL(state, toolId) {
      state.tools = state.tools.filter(t => t.id !== toolId)
    },
    SET_EMPLOYEES(state, employees) {
      state.employees = employees
    },
    SET_CURRENT_EMPLOYEE(state, employee) {
      state.currentEmployee = employee
    },
    SET_WORKCENTERS(state, workcenters) {
      state.workcenters = workcenters
    },
    SET_CURRENT_WORKCENTER(state, workcenter) {
      state.currentWorkCenter = workcenter
    },
    SET_LOADING(state, loading) {
      state.loading = loading
    },
    SET_ERROR(state, error) {
      state.error = error
    }
  },
  actions: {
    async fetchTools({ commit }) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.get('/api/tools/')
        commit('SET_TOOLS', response.data)
      } catch (error) {
        commit('SET_ERROR', error.message)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async fetchTool({ commit }, id) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.get(`/api/tools/${id}/`)
        commit('SET_CURRENT_TOOL', response.data)
      } catch (error) {
        commit('SET_ERROR', error.message)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async createTool({ commit }, toolData) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.post('/api/tools/', toolData)
        commit('ADD_TOOL', response.data)
        return response.data
      } catch (error) {
        commit('SET_ERROR', error.message)
        throw error
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async updateTool({ commit }, { id, toolData }) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.put(`/api/tools/${id}/`, toolData)
        commit('UPDATE_TOOL', response.data)
        return response.data
      } catch (error) {
        commit('SET_ERROR', error.message)
        throw error
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async deleteTool({ commit }, id) {
      commit('SET_LOADING', true)
      try {
        await axios.delete(`/api/tools/${id}/`)
        commit('DELETE_TOOL', id)
      } catch (error) {
        commit('SET_ERROR', error.message)
        throw error
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async fetchEmployees({ commit }) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.get('/api/employees/')
        commit('SET_EMPLOYEES', response.data)
      } catch (error) {
        commit('SET_ERROR', error.message)
      } finally {
        commit('SET_LOADING', false)
      }
    },
    async fetchWorkCenters({ commit }) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.get('/api/workcenters/')
        commit('SET_WORKCENTERS', response.data)
      } catch (error) {
        commit('SET_ERROR', error.message)
      } finally {
        commit('SET_LOADING', false)
      }
    }
  }
})
