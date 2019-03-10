import treeTemp from '../../temp_data/cabecalhoLido.json'
import axios from 'axios'
const state = {
  indicadores: {}
}

export const getters = {
  indicadoresDe: state => cidade => {
    return state.indicadores[cidade] || []
  },
  getIndicadores: state => {
    return state.indicadores
  }

}

export const mutations = {
  initIndicadores (state, newData) {
    state.indicadores = newData
  },
  updateIndicadores (state, newData) {
    state.indicadores = newData
  }
}

export const actions = {

  initIndicadores (context) {
    context.commit('initIndicadores', [{ text: 'batata' }])
  },

  getIndicadoresById (context, { idMacroindicador }) {
    axios.get(`/api/macroindicador/${idMacroindicador}/indicadores`)
      .then((response) => {
        context.commit('updateIndicadores', response)
      }).catch((error) => {
        console.error(error)
      })
  },

  getIndicadoresByLocalidade (context, { idLocalidade }) {
    if (idLocalidade === '2') {
      context.commit('updateIndicadores', treeTemp)
      console.log(treeTemp)
    }
    // axios.get(`/api/localidade/${idLocalidade}/macroindicadores`)
    //   .then((response) => {
    //     context.commit('updateIndicadores', response)
    //   }).catch((error) => {
    //     console.error(error)
    //   })
  }

}

export default {
  state,
  getters,
  mutations,
  actions
}
