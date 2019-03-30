// https://vuex.vuejs.org/en/getters.html

export default {
  getMacroindicadores: state => {
    return state.macroindicadores || []
  },
  getMacroindicadorById: state => id => {
    console.log(state.macroindicadores.filter(m => { return m.id === id }))
    return state.macroindicadores.filter(m => { return m.id === id })[0] || []
  }
}
