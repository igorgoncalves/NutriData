// https://vuex.vuejs.org/en/getters.html

export default {
  getNotificacoes: state => {
    return state.notificacoes || []
  },
  getNotificacoesStatus: state => {
    return state.notificacoesStatus
  }
}
