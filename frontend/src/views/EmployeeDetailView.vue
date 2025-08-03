<template>
  <div class="employee-detail">
    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else-if="error" class="alert alert-danger" role="alert">
      {{ error }}
    </div>

    <div v-else-if="employee" class="row">
      <div class="col-lg-4 mb-4 mb-lg-0">
        <div class="card shadow h-100">
          <div class="card-body text-center pt-4">
            <div class="avatar-large bg-primary text-white mx-auto mb-3">
              {{ getInitials(employee) }}
            </div>

            <h2 class="card-title">{{ employee.first_name }} {{ employee.last_name }}</h2>
            <p class="text-muted" v-if="employee.position">{{ employee.position }}</p>
            <p class="text-muted" v-if="employee.department">{{ employee.department }}</p>

            <div class="d-flex justify-content-center mt-4">
              <router-link :to="`/employees/${employee.id}/edit`" class="btn btn-primary me-2">
                <i class="bi bi-pencil"></i> Edit
              </router-link>
              <button @click="confirmDelete" class="btn btn-danger">
                <i class="bi bi-trash"></i> Delete
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-8">
        <div class="card shadow mb-4">
          <div class="card-header bg-light">
            <h3 class="mb-0 fs-5">Contact Information</h3>
          </div>
          <div class="card-body">
            <div class="row mb-3" v-if="employee.email">
              <div class="col-md-3 text-muted">Email</div>
              <div class="col-md-9">
                <a :href="`mailto:${employee.email}`">{{ employee.email }}</a>
              </div>
            </div>
            <div class="row mb-3" v-if="employee.phone">
              <div class="col-md-3 text-muted">Phone</div>
              <div class="col-md-9">{{ employee.phone }}</div>
            </div>
            <div class="row" v-if="employee.employee_id">
              <div class="col-md-3 text-muted">Employee ID</div>
              <div class="col-md-9">{{ employee.employee_id }}</div>
            </div>
          </div>
        </div>

        <div class="card shadow">
          <div class="card-header bg-light d-flex justify-content-between align-items-center">
            <h3 class="mb-0 fs-5">Assigned Tools</h3>
            <button class="btn btn-sm btn-outline-primary" @click="toggleAssignTool">
              <i class="bi bi-plus-circle"></i> Assign Tool
            </button>
          </div>

          <div class="card-body">
            <div v-if="showAssignToolForm" class="mb-4 p-3 border rounded bg-light">
              <h4 class="fs-6 mb-3">Assign a Tool</h4>
              <div class="row g-3">
                <div class="col-md-8">
                  <select class="form-select" v-model="selectedToolId">
                    <option value="" disabled selected>Select a tool</option>
                    <option v-for="tool in availableTools" :key="tool.id" :value="tool.id">
                      {{ tool.name }} ({{ tool.serial_number }})
                    </option>
                  </select>
                </div>
                <div class="col-md-4 d-flex">
                  <button
                    class="btn btn-primary me-2"
                    @click="assignTool"
                    :disabled="!selectedToolId || assigningTool"
                  >
                    <span v-if="assigningTool" class="spinner-border spinner-border-sm me-1"></span>
                    Assign
                  </button>
                  <button class="btn btn-outline-secondary" @click="toggleAssignTool">
                    Cancel
                  </button>
                </div>
              </div>
            </div>

            <div v-if="!employee.assigned_tools?.length" class="text-center text-muted py-4">
              <i class="bi bi-tools fs-3"></i>
              <p class="mt-2">No tools currently assigned to this employee.</p>
            </div>

            <div v-else class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th>Tool Name</th>
                    <th>Serial Number</th>
                    <th>Calibrated</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="tool in employee.assigned_tools" :key="tool.id">
                    <td>{{ tool.name }}</td>
                    <td>{{ tool.serial_number }}</td>
                    <td>
                      <span :class="tool.calibrated ? 'badge bg-success' : 'badge bg-warning'">
                        {{ tool.calibrated ? 'Yes' : 'No' }}
                      </span>
                    </td>
                    <td>
                      <div class="btn-group btn-group-sm">
                        <router-link :to="`/tools/${tool.id}`" class="btn btn-outline-secondary">
                          <i class="bi bi-eye"></i>
                        </router-link>
                        <button @click="unassignTool(tool.id)" class="btn btn-outline-danger">
                          <i class="bi bi-x-circle"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal fade" id="deleteEmployeeModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirm Delete</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Are you sure you want to delete <strong>{{ employee?.first_name }} {{ employee?.last_name }}</strong>?
            This action cannot be undone.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button @click="deleteEmployee" type="button" class="btn btn-danger">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { Modal } from 'bootstrap'

export default {
  name: 'EmployeeDetailView',
  setup() {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()

    const deleteModal = ref(null)
    const showAssignToolForm = ref(false)
    const selectedToolId = ref('')
    const assigningTool = ref(false)

    const employee = computed(() => store.state.currentEmployee)
    const tools = computed(() => store.state.tools)
    const loading = computed(() => store.state.loading)
    const error = computed(() => store.state.error)

    const availableTools = computed(() => {
      const assignedIds = employee.value?.assigned_tools?.map(t => t.id) || []
      return tools.value.filter(tool => !assignedIds.includes(tool.id))
    })

    onMounted(async () => {
      const employeeId = route.params.id
      await Promise.all([
        store.dispatch('fetchEmployee', employeeId),
        store.dispatch('fetchTools')
      ])
    })

    const getInitials = (employee) => {
      return `${employee.first_name[0]}${employee.last_name[0]}`.toUpperCase()
    }

    const toggleAssignTool = () => {
      showAssignToolForm.value = !showAssignToolForm.value
      if (!showAssignToolForm.value) {
        selectedToolId.value = ''
      }
    }

    const assignTool = async () => {
      if (!selectedToolId.value) return

      assigningTool.value = true
      try {
        await store.dispatch('assignToolToEmployee', {
          employeeId: employee.value.id,
          toolId: selectedToolId.value
        })
        showAssignToolForm.value = false
        selectedToolId.value = ''
      } catch (err) {
        console.error('Error assigning tool:', err)
      } finally {
        assigningTool.value = false
      }
    }

    const unassignTool = async (toolId) => {
      try {
        await store.dispatch('unassignToolFromEmployee', {
          employeeId: employee.value.id,
          toolId
        })
      } catch (err) {
        console.error('Error unassigning tool:', err)
      }
    }

    const confirmDelete = () => {
      if (!deleteModal.value) {
        deleteModal.value = new Modal(document.getElementById('deleteEmployeeModal'))
      }
      deleteModal.value.show()
    }

    const deleteEmployee = async () => {
      try {
        await store.dispatch('deleteEmployee', employee.value.id)
        deleteModal.value.hide()
        router.push('/employees')
      } catch (err) {
        console.error('Error deleting employee:', err)
      }
    }

    return {
      employee,
      loading,
      error,
      availableTools,
      getInitials,
      confirmDelete,
      deleteEmployee,
      showAssignToolForm,
      toggleAssignTool,
      selectedToolId,
      assigningTool,
      assignTool,
      unassignTool
    }
  }
}
</script>

<style scoped>
.employee-detail {
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.avatar-large {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: bold;
}
</style>
