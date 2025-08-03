<template>
  <div class="employees-container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1>Employees</h1>
      <router-link to="/employees/create" class="btn btn-primary">
        <i class="bi bi-person-plus me-1"></i> Add Employee
      </router-link>
    </div>

    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else-if="error" class="alert alert-danger" role="alert">
      {{ error }}
    </div>

    <div v-else-if="!employees.length" class="alert alert-info" role="alert">
      No employees found. Click the "Add Employee" button to add one.
    </div>

    <div v-else>
      <!-- Search and filter -->
      <div class="card shadow-sm mb-4">
        <div class="card-body">
          <div class="row g-3">
            <div class="col-md-6">
              <div class="input-group">
                <span class="input-group-text bg-light">
                  <i class="bi bi-search"></i>
                </span>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Search employees..."
                  v-model="searchQuery"
                >
              </div>
            </div>
            <div class="col-md-6">
              <div class="d-flex justify-content-md-end">
                <div class="btn-group">
                  <button type="button" class="btn btn-outline-primary" @click="sortBy('last_name')">
                    Sort by Name
                    <i v-if="sortField === 'last_name'"
                       :class="sortDirection === 'asc' ? 'bi bi-sort-alpha-down' : 'bi bi-sort-alpha-up'"></i>
                  </button>
                  <button type="button" class="btn btn-outline-primary" @click="sortBy('department')">
                    Sort by Department
                    <i v-if="sortField === 'department'"
                       :class="sortDirection === 'asc' ? 'bi bi-sort-alpha-down' : 'bi bi-sort-alpha-up'"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Employees list -->
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        <div v-for="employee in filteredEmployees" :key="employee.id" class="col">
          <div class="card h-100 shadow-sm hover-card">
            <div class="card-body">
              <div class="d-flex align-items-center mb-3">
                <div class="avatar bg-primary text-white me-3">
                  {{ getInitials(employee) }}
                </div>
                <div>
                  <h5 class="card-title mb-0">
                    {{ employee.first_name }} {{ employee.last_name }}
                  </h5>
                  <p class="text-muted mb-0" v-if="employee.department">
                    {{ employee.department }}
                  </p>
                </div>
              </div>

              <div class="employee-details">
                <div class="mb-2" v-if="employee.position">
                  <i class="bi bi-briefcase me-2"></i>
                  {{ employee.position }}
                </div>
                <div class="mb-2" v-if="employee.email">
                  <i class="bi bi-envelope me-2"></i>
                  <a :href="`mailto:${employee.email}`">{{ employee.email }}</a>
                </div>
                <div v-if="employee.phone">
                  <i class="bi bi-telephone me-2"></i>
                  {{ employee.phone }}
                </div>
              </div>

              <div v-if="employee.assigned_tools && employee.assigned_tools.length > 0">
                <hr>
                <h6><i class="bi bi-tools me-2"></i> Assigned Tools:</h6>
                <ul class="list-unstyled">
                  <li v-for="tool in employee.assigned_tools" :key="tool.id">
                    <small>{{ tool.name }}</small>
                  </li>
                </ul>
              </div>
            </div>

            <div class="card-footer bg-white border-top-0">
              <div class="d-flex justify-content-between">
                <router-link :to="`/employees/${employee.id}`" class="btn btn-sm btn-outline-primary">
                  <i class="bi bi-eye me-1"></i> View
                </router-link>
                <div class="btn-group btn-group-sm">
                  <router-link :to="`/employees/${employee.id}/edit`" class="btn btn-outline-secondary">
                    <i class="bi bi-pencil"></i> Edit
                  </router-link>
                  <button @click="confirmDelete(employee)" class="btn btn-outline-danger">
                    <i class="bi bi-trash"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal fade" id="deleteEmployeeModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirm Delete</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Are you sure you want to delete <strong>{{ employeeToDelete?.first_name }} {{ employeeToDelete?.last_name }}</strong>?
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
import { Modal } from 'bootstrap'

export default {
  name: 'EmployeesView',
  setup() {
    const store = useStore()
    const searchQuery = ref('')
    const sortField = ref('last_name')
    const sortDirection = ref('asc')
    const employeeToDelete = ref(null)
    const deleteModal = ref(null)

    const employees = computed(() => store.state.employees)
    const loading = computed(() => store.state.loading)
    const error = computed(() => store.state.error)

    onMounted(() => {
      store.dispatch('fetchEmployees')
    })

    const filteredEmployees = computed(() => {
      let result = [...employees.value]

      // Apply search filter
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        result = result.filter(employee =>
          employee.first_name.toLowerCase().includes(query) ||
          employee.last_name.toLowerCase().includes(query) ||
          (employee.department && employee.department.toLowerCase().includes(query))
        )
      }

      // Apply sorting
      result.sort((a, b) => {
        let fieldA = a[sortField.value] || ''
        let fieldB = b[sortField.value] || ''

        if (sortField.value === 'last_name') {
          fieldA = `${a.last_name} ${a.first_name}`
          fieldB = `${b.last_name} ${b.first_name}`
        }

        return sortDirection.value === 'asc'
          ? fieldA.localeCompare(fieldB)
          : fieldB.localeCompare(fieldA)
      })

      return result
    })

    const sortBy = (field) => {
      if (sortField.value === field) {
        sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
      } else {
        sortField.value = field
        sortDirection.value = 'asc'
      }
    }

    const getInitials = (employee) => {
      return `${employee.first_name[0]}${employee.last_name[0]}`.toUpperCase()
    }

    const confirmDelete = (employee) => {
      employeeToDelete.value = employee

      if (!deleteModal.value) {
        deleteModal.value = new Modal(document.getElementById('deleteEmployeeModal'))
      }
      deleteModal.value.show()
    }

    const deleteEmployee = async () => {
      try {
        await store.dispatch('deleteEmployee', employeeToDelete.value.id)
        deleteModal.value.hide()
      } catch (err) {
        console.error('Error deleting employee:', err)
      }
    }

    return {
      employees,
      loading,
      error,
      searchQuery,
      sortField,
      sortDirection,
      filteredEmployees,
      sortBy,
      getInitials,
      confirmDelete,
      deleteEmployee,
      employeeToDelete
    }
  }
}
</script>

<style scoped>
.employees-container {
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.hover-card {
  transition: transform 0.2s, box-shadow 0.2s;
}

.hover-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1) !important;
}
</style>
