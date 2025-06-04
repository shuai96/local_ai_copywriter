import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'copywriter',
      component: () => import('../views/CopyWriterView.vue'),
    },
  ],
})

export default router
