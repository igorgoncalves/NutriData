// https://vuex.vuejs.org/en/getters.html

export default {
  getLocalidades: state => {
    return state.localidades || []
  },
  getLocalidadeName: state => codigo => {
    let localidade = state.localidades.filter(el => el.codigo == codigo)

    return localidade.length > 0 ? localidade[0].nome : ''
  }
}
