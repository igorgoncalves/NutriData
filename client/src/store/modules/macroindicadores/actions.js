import Vue from 'vue'

// https://vuex.vuejs.org/en/actions.html
export default {
  initMacroindicadores (context) {
    context.commit('initMacroindicadores')
  },

  fetchMacroindicadores (context) {
    Vue.prototype.$http.get(`/api/macroindicadores`)
      .then((response) => {
        context.commit('updateMacroindicadores', response.data)
      }).catch((error) => {
        console.error(error)
      })
  }
}
