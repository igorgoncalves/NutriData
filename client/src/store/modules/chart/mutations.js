// https://vuex.vuejs.org/en/mutations.html

export default {
  load (state, payload) {
    state.idMacroindicador = payload.idMacroindicador
    state.idLocalidade = payload.idLocalidade
  }
}
