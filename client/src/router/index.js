import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/about', component: 'About' },
  { path: '/visoes', component: 'Visoes/List' },
  { path: '/visoes/insert', component: 'Visoes/Insert' },
  { path: '/visoes/list', component: 'Visoes/List' },
  { path: '/macroindicador', component: 'Macroindicador/List' },
  { path: '/macroindicador/insert', component: 'Macroindicador/Insert' },
  { path: '/macroindicador/list', component: 'Macroindicador/List' },
  { path: '*', component: 'Default/NotFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/Pages/${route.component}.vue`)
  }
})

export default new Router({
  routes,
  mode: 'history'
})
