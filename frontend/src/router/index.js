import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/tools'
  },
  {
    path: '/tools',
    name: 'tools',
    component: () => import('../views/ToolsView.vue')
  },
  {
    path: '/tools/:id',
    name: 'toolDetail',
    component: () => import('../views/ToolDetailView.vue')
  },
  {
    path: '/tools/create',
    name: 'toolCreate',
    component: () => import('../views/ToolFormView.vue')
  },
  {
    path: '/employees',
    name: 'employees',
    component: () => import('../views/EmployeesView.vue')
  },
  {
    path: '/employees/:id',
    name: 'employeeDetail',
    component: () => import('../views/EmployeeDetailView.vue')
  },
  {
    path: '/workcenters',
    name: 'workcenters',
    component: () => import('../views/WorkCentersView.vue')
  },
  {
    path: '/workcenters/:id',
    name: 'workcenterDetail',
    component: () => import('../views/WorkCenterDetailView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: 'active'
})

export default router
