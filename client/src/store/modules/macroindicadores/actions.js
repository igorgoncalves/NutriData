import Vue from 'vue'

// https://vuex.vuejs.org/en/actions.html
export default {
  initMacroindicadores (context) {
    context.commit('initMacroindicadores')
  },

  fetchMacroindicadores (context, codigoLocalidade) {
    Vue.prototype.$http.get(`/api/macroindicador/${codigoLocalidade}`)
      .then((response) => {
        context.commit('updateMacroindicadores', response.data)
      }).catch((error) => {
        console.error(error)
      })
  }
}
