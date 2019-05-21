// https://vuex.vuejs.org/en/getters.html

export default {
  getMacroindicadores: state => {
    return state.macroindicadores || []
  },
  getMacroindicadorById: state => id => {
    return state.macroindicadores.filter(m => { return m.id === id })[0] || []
  },
  getMacroindicadorAndVisao: state => {
    return state.macroindicador || {}
  },
  getMacroindicadorByLocalidade: state => idLocalidade => {
    return state.macroindicadores.filter(function (el) {
      console.log(el)
      return true
    })
  }
}
