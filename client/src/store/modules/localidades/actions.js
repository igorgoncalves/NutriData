import Vue from 'vue'

// https://vuex.vuejs.org/en/actions.html
export default {
  initLocalidades (context) {
    context.commit('initLocalidades')
  },

  fetchLocalidades (context) {
    Vue.prototype.$http.get(`/api/localidade`)
      .then((response) => {
        context.commit('updateLocalidades', response.data)
      }).catch((error) => {
        console.error(error)
      })
  }
}
