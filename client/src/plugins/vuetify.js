import Vue from 'vue'
import Vuetify from 'vuetify'
import theme from './theme'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.use(Vuetify, {
  iconfont: 'mdi',
  theme
});


import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css';


import { TiptapVuetifyPlugin } from 'tiptap-vuetify';
import 'tiptap-vuetify/dist/main.css';

// Vuetify Object (as described in the Vuetify 2 documentation)
// const vuetify = new Vuetify();

Vue.use(TiptapVuetifyPlugin, {  
  iconsGroup: 'mdi',
  // vuetify : vuetify
});
