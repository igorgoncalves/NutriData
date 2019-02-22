import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/about', component: 'About' },
  { path: '/dimension', component: 'Dimension/List' },
  { path: '/dimension/insert', component: 'Dimension/Insert' },
  { path: '/dimension/list', component: 'Dimension/List' },
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
