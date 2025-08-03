<template>
  <div class="tool-detail">
    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else-if="error" class="alert alert-danger" role="alert">
      {{ error }}
    </div>

    <div v-else-if="tool" class="card shadow">
      <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
        <h2 class="mb-0 fs-4">Tool Details</h2>
        <div>
          <router-link :to="`/tools/${tool.id}/edit`" class="btn btn-light btn-sm me-2">
            <i class="bi bi-pencil"></i> Edit
          </router-link>
          <button @click="confirmDelete" class="btn btn-danger btn-sm">
            <i class="bi bi-trash"></i> Delete
          </button>
        </div>
      </div>

      <div class="card-body">
        <div class="row">
          <div class="col-md-6">
            <h3 class="fs-5">{{ tool.name }}</h3>
            <p class="text-muted">Serial Number: {{ tool.serial_number }}</p>

            <div class="mb-3">
              <span class="me-2">Calibration Status:</span>
              <span :class="tool.calibrated ? 'badge bg-success' : 'badge bg-warning'">
                {{ tool.calibrated ? 'Calibrated' : 'Not Calibrated' }}
              </span>
            </div>

            <p>
              <strong>Last Checked In:</strong>
              <span v-if="tool.last_checked_in">{{ formatDate(tool.last_checked_in) }}</span>
              <span v-else class="text-muted">Never</span>
            </p>
          </div>

          <div class="col-md-6" v-if="tool.assigned_to || tool.workcenter">
            <div class="card bg-light">
              <div class="card-body">
                <h4 class="fs-6">Assignment Information</h4>
                <div v-if="tool.assigned_to">
                  <p class="mb-1"><strong>Assigned To:</strong></p>
                  <p>{{ tool.assigned_to.first_name }} {{ tool.assigned_to.last_name }}</p>
                </div>
                <div v-if="tool.workcenter">
                  <p class="mb-1"><strong>Work Center:</strong></p>
                  <p>{{ tool.workcenter.name }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card-footer">
        <router-link to="/tools" class="btn btn-outline-secondary">
          <i class="bi bi-arrow-left"></i> Back to Tools
        </router-link>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal fade" id="deleteToolModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirm Delete</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Are you sure you want to delete <strong>{{ tool?.name }}</strong>?
            This action cannot be undone.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button @click="deleteTool" type="button" class="btn btn-danger">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { Modal } from 'bootstrap'

export default {
  name: 'ToolDetailView',
  setup() {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()
    const deleteModal = ref(null)

    const tool = computed(() => store.state.currentTool)
    const loading = computed(() => store.state.loading)
    const error = computed(() => store.state.error)

    onMounted(async () => {
      const toolId = route.params.id
      await store.dispatch('fetchTool', toolId)
    })

    const formatDate = (dateString) => {
      if (!dateString) return 'Never'
      const date = new Date(dateString)
      return new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      }).format(date)
    }

    const confirmDelete = () => {
      if (!deleteModal.value) {
        deleteModal.value = new Modal(document.getElementById('deleteToolModal'))
      }
      deleteModal.value.show()
    }

    const deleteTool = async () => {
      try {
        await store.dispatch('deleteTool', tool.value.id)
        deleteModal.value.hide()
        router.push('/tools')
      } catch (err) {
        console.error('Error deleting tool:', err)
      }
    }

    return {
      tool,
      loading,
      error,
      formatDate,
      confirmDelete,
      deleteTool
    }
  }
}
</script>

<style scoped>
.tool-detail {
  animation: fadeIn 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
