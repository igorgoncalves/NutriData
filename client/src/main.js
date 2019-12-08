// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueMq from 'vue-mq';

Vue.use(VueMq, {
  breakpoints: {
    xs: 600,
    sm: 960,
    md: 1264,
    lg: 1904,
    xl: Infinity
  }
});

// Components
import './components';

// Plugins
import './plugins';

// Sync router with store
import { sync } from 'vuex-router-sync';

// Application imports
import App from './App';
import i18n from '@/i18n';
import router from '@/router';
import store from '@/store';

import publicTemplate from "./views/Templates/Public";
import adminTemplate from "./views/Templates/Admin";

Vue.component('public-template', publicTemplate);
Vue.component('admin-template', adminTemplate);

// Sync store with router
sync(store, router);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app');
