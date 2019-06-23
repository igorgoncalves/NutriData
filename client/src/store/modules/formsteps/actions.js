
// https://vuex.vuejs.org/en/actions.html
export default {
  nextStep (context) {
    context.commit('nextStep')
  },
  reset (context) {
    context.commit('reset')
  }
}
