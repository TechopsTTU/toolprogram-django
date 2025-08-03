<template>
  <div class="tool-form">
    <div class="card shadow">
      <div class="card-header bg-primary text-white">
        <h2 class="mb-0 fs-4">{{ isEditMode ? 'Edit Tool' : 'Add New Tool' }}</h2>
      </div>

      <div class="card-body">
        <form @submit.prevent="saveTool">
          <div class="mb-3">
            <label for="name" class="form-label">Tool Name*</label>
            <input
              type="text"
              class="form-control"
              id="name"
              v-model="form.name"
              required
              :class="{ 'is-invalid': errors.name }"
            >
            <div v-if="errors.name" class="invalid-feedback">{{ errors.name }}</div>
          </div>

          <div class="mb-3">
            <label for="serial_number" class="form-label">Serial Number*</label>
            <input
              type="text"
              class="form-control"
              id="serial_number"
              v-model="form.serial_number"
              required
              :class="{ 'is-invalid': errors.serial_number }"
            >
            <div v-if="errors.serial_number" class="invalid-feedback">{{ errors.serial_number }}</div>
          </div>

          <div class="form-check mb-3">
            <input
              type="checkbox"
              class="form-check-input"
              id="calibrated"
              v-model="form.calibrated"
            >
            <label class="form-check-label" for="calibrated">Calibrated</label>
          </div>

          <div class="mb-3">
            <label for="workcenter" class="form-label">Work Center</label>
            <select
              class="form-select"
              id="workcenter"
              v-model="form.workcenter"
              :class="{ 'is-invalid': errors.workcenter }"
            >
              <option value="">-- None --</option>
              <option v-for="wc in workcenters" :key="wc.id" :value="wc.id">
                {{ wc.name }}
              </option>
            </select>
            <div v-if="errors.workcenter" class="invalid-feedback">{{ errors.workcenter }}</div>
          </div>

          <div class="mb-3">
            <label for="employee" class="form-label">Assigned Employee</label>
            <select
              class="form-select"
              id="employee"
              v-model="form.assigned_to"
              :class="{ 'is-invalid': errors.assigned_to }"
            >
              <option value="">-- None --</option>
              <option v-for="emp in employees" :key="emp.id" :value="emp.id">
                {{ emp.first_name }} {{ emp.last_name }}
              </option>
            </select>
            <div v-if="errors.assigned_to" class="invalid-feedback">{{ errors.assigned_to }}</div>
          </div>

          <div class="d-flex justify-content-between mt-4">
            <router-link to="/tools" class="btn btn-outline-secondary">
              Cancel
            </router-link>
            <button type="submit" class="btn btn-primary" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status"></span>
              {{ isEditMode ? 'Update Tool' : 'Create Tool' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, reactive, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'ToolFormView',
  setup() {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()

    const toolId = route.params.id
    const isEditMode = computed(() => !!toolId)

    const form = reactive({
      name: '',
      serial_number: '',
      calibrated: false,
      workcenter: '',
      assigned_to: ''
    })

    const errors = reactive({})
    const loading = computed(() => store.state.loading)
    const workcenters = computed(() => store.state.workcenters)
    const employees = computed(() => store.state.employees)

    onMounted(async () => {
      // Fetch workcenters and employees for dropdowns
      await store.dispatch('fetchWorkCenters')
      await store.dispatch('fetchEmployees')

      // If editing, populate the form with existing tool data
      if (isEditMode.value) {
        await store.dispatch('fetchTool', toolId)
        const tool = store.state.currentTool
        if (tool) {
          form.name = tool.name
          form.serial_number = tool.serial_number
          form.calibrated = tool.calibrated || false
          form.workcenter = tool.workcenter ? tool.workcenter.id : ''
          form.assigned_to = tool.assigned_to ? tool.assigned_to.id : ''
        }
      }
    })

    const validateForm = () => {
      errors.name = !form.name ? 'Tool name is required' : null
      errors.serial_number = !form.serial_number ? 'Serial number is required' : null

      return !Object.values(errors).some(error => error)
    }

    const saveTool = async () => {
      if (!validateForm()) return

      try {
        if (isEditMode.value) {
          await store.dispatch('updateTool', {
            id: toolId,
            toolData: { ...form }
          })
        } else {
          await store.dispatch('createTool', { ...form })
        }

        router.push('/tools')
      } catch (error) {
        console.error('Error saving tool:', error)
        if (error.response?.data) {
          // Handle API validation errors
          const apiErrors = error.response.data
          Object.keys(apiErrors).forEach(key => {
            errors[key] = apiErrors[key].join(' ')
          })
        }
      }
    }

    return {
      form,
      errors,
      loading,
      isEditMode,
      workcenters,
      employees,
      saveTool
    }
  }
}
</script>

<style scoped>
.tool-form {
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

