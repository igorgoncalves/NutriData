// https://vuex.vuejs.org/en/getters.html

export default {
  indicadoresDe: state => cidade => {
    return state.indicadores[cidade] || []
  },
  getIndicadores: state => {
    return state.indicadores
  }
}
