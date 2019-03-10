import cabecalhoLido from '../../temp_data/cabecalhoLido.json'

const state = {
  sheetHeaders: []
}

export const getters = {
  indicadoresDeCidades: state => cidade => {
    return state.indicadores[cidade] || []
  }
}

export const mutations = {
  setSheetHeaders (state, payload) {
    state.blackCards = payload
  }
}

export const actions = {
  fetchIndicadores ({ commit }) {
    commit('setSheetHeaders', cabecalhoLido)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
