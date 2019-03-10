import Vue from 'vue'
import Vuex from 'vuex'
import indicadores from './modules/indicadores'
import upload from './modules/upload'

Vue.use(Vuex)

// const debug = process.env.NODE_ENV !== 'production'
const debug = true

export default new Vuex.Store({
  modules: {
    indicadores,
    upload
  },
  strict: debug
})
