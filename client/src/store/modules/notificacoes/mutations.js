// https://vuex.vuejs.org/en/mutations.html

export default {
  initNotificacoes (state, payload) {
    state.notificacoes = payload
  },
  updateNotificacoes (state, payload) {
    state.notificacoes = payload
  },
  updateNotificacoesStatus (state, payload) {
    state.notificacoesStatus = payload
  }
}
