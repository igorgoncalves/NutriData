import Vue from 'vue'
import treeTemp from './cabecalhoLido.json'
// https://vuex.vuejs.org/en/actions.html

export default {
  initIndicadores (context) {
    context.commit('initIndicadores', [{ text: 'batata' }])
  },

  getIndicadoresById (context, { idMacroindicador }) {
    if (typeof idMacroindicador === 'object') {
      console.log(idMacroindicador)
      idMacroindicador = idMacroindicador.values()
    }

    Vue.prototype.$http.get(`/api/macroindicador/${idMacroindicador}/indicadores`)
      .then((response) => {
        context.commit('updateIndicadores', response.data)
      }).catch((error) => {
        console.error(error)
      })
  },

  getIndicadoresByLocalidade (context, { idLocalidade }) {
    if (idLocalidade === '2') {
      context.commit('updateIndicadores', treeTemp)
    }
    // axios.get(`/api/localidade/${idLocalidade}/macroindicadores`)
    //   .then((response) => {
    //     context.commit('updateIndicadores', response)
    //   }).catch((error) => {
    //     console.error(error)
    //   })
  }
}
