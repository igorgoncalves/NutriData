// https://vuex.vuejs.org/en/getters.html

export default {
  getMacroindicadores: state => {
    return state.macroindicadores || []
  }
}
