// https://vuex.vuejs.org/en/state.html

const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: {}, user: null }

export default {
  state: initialState
}
