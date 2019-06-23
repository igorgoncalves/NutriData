
export default {
  nextStep (state) {
    state.formProgress++
  },
  reset (state) {
    state.formProgress = 1
  }
}
