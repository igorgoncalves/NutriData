/**
 * Vue Router
 *
 * @library
 *
 * https://router.vuejs.org/en/
 */

// Lib imports
import Vue from 'vue';
// import VueAnalytics from 'vue-analytics'
import Router from 'vue-router';
import Meta from 'vue-meta';

// Routes
import paths from './paths';

function route (path, view, name, type) {
  return {
    name: name || view,
    path,
    meta: { layout: type },
    component: (resovle) => import(
      `@/views/${view}.vue`
    ).then(resovle)
  }
}

Vue.use(Router);

// Create a new router
const router = new Router({
  mode: 'history',
  routes: paths.map(path => route(path.path, path.view, path.name, path.type)).concat([
    { path: '*', view: 'Home' }    
  ]),
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }
    if (to.hash) {
      return { selector: to.hash }
    }
    return { x: 0, y: 0 };
  }
});


router.afterEach((to, from) => {
  console.log(to);
  console.log(from);
})


router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['Home','Login','PublicaMacroindicadorVisao'];
  const authRequired = !publicPages.includes(to.name);

  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {    
    return next('/login');
  }

  next();
})

Vue.use(Meta);

// // Bootstrap Analytics
// // Set in .env
// // https://github.com/MatteoGabriele/vue-analytics
// if (process.env.GOOGLE_ANALYTICS) {
//   Vue.use(VueAnalytics, {
//     id: process.env.GOOGLE_ANALYTICS,
//     router,
//     autoTracking: {
//       page: process.env.NODE_ENV !== 'development'
//     }
//   })
// }

export default router;
