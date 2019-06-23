// https://vuex.vuejs.org/en/mutations.html

export default {
  getAllRequest (state) {
    state.all = { loading: true }
  },
  getAllSuccess (state, users) {
    state.all = { items: users }
  },
  getAllFailure (state, error) {
    state.all = { error }
  }
}
