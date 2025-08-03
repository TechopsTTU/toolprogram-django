<template>
  <div class="tools-container">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1>Tools</h1>
      <router-link to="/tools/create" class="btn btn-primary">
        <i class="bi bi-plus-circle me-1"></i> Add New Tool
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

    <div v-else-if="!tools.length" class="alert alert-info" role="alert">
      No tools found. Click the "Add New Tool" button to create one.
    </div>

    <div v-else class="card shadow-sm mb-4">
      <div class="table-responsive">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th>Name</th>
              <th>Serial Number</th>
              <th>Calibrated</th>
              <th>Last Checked</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="tool in tools" :key="tool.id">
              <td>{{ tool.name }}</td>
              <td>{{ tool.serial_number }}</td>
              <td>
                <span :class="tool.calibrated ? 'badge bg-success' : 'badge bg-warning'">
                  {{ tool.calibrated ? 'Yes' : 'No' }}
                </span>
              </td>
              <td>{{ formatDate(tool.last_checked_in) }}</td>
              <td>
                <div class="btn-group btn-group-sm">
                  <router-link :to="`/tools/${tool.id}`" class="btn btn-outline-primary">
                    <i class="bi bi-eye"></i> View
                  </router-link>
                  <router-link :to="`/tools/${tool.id}/edit`" class="btn btn-outline-secondary">
                    <i class="bi bi-pencil"></i> Edit
                  </router-link>
                  <button @click="confirmDelete(tool)" class="btn btn-outline-danger">
                    <i class="bi bi-trash"></i> Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal fade" id="deleteToolModal" tabindex="-1" aria-labelledby="deleteToolModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="deleteToolModalLabel">Confirm Delete</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Are you sure you want to delete the tool <strong>{{ toolToDelete?.name }}</strong>?
            This action cannot be undone.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-danger" @click="deleteTool">Delete</button>
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
  name: 'ToolsView',
  setup() {
    const store = useStore()
    const toolToDelete = ref(null)
    const deleteModal = ref(null)

    const tools = computed(() => store.getters.getTools)
    const loading = computed(() => store.state.loading)
    const error = computed(() => store.state.error)

    onMounted(() => {
      store.dispatch('fetchTools')
    })

    const formatDate = (dateString) => {
      if (!dateString) return 'Never'
      const date = new Date(dateString)
      return date.toLocaleDateString()
    }

    const confirmDelete = (tool) => {
      toolToDelete.value = tool

      // Use Bootstrap modal
      if (!deleteModal.value) {
        deleteModal.value = new Modal(document.getElementById('deleteToolModal'))
      }
      deleteModal.value.show()
    }

    const deleteTool = async () => {
      try {
        await store.dispatch('deleteTool', toolToDelete.value.id)
        deleteModal.value.hide()
      } catch (err) {
        console.error('Error deleting tool:', err)
      }
    }

    return {
      tools,
      loading,
      error,
      formatDate,
      confirmDelete,
      deleteTool,
      toolToDelete
    }
  }
}
</script>

<style scoped>
.tools-container {
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
