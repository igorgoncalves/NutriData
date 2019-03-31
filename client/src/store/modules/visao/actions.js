import Vue from 'vue'

// https://vuex.vuejs.org/en/actions.html
export default {
  initVisao (context) {
    context.commit('initVisao')
  },

  fetchVisao (context, idVisao) {
    Vue.prototype.$http.get(`/api/visao${idVisao}`)
      .then((response) => {
        context.commit('updateVisao', response.data)
      }).catch((error) => {
        console.error(error)
      })
  },
  createVisao (context, data, idMacroindicador) {
    Vue.prototype.$http.post(`/api/macroindicador/${data.idMacroindicador}/visao`, data)
      .then((response) => {
        console.log(response)
        context.commit('updateVisao', response.data)
      }).catch((error) => {
        console.error(error)
      })
  }
}
