import { userService } from '../../../services'
import router from '../../../router'
// https://vuex.vuejs.org/en/actions.html

export default {
  login ({ dispatch, commit }, { username, password }) {
    commit('loginRequest', { username })

    userService.login(username, password)
      .then(
        user => {
          commit('loginSuccess', user)
          router.push('/macroindicadores')
        },
        error => {
          commit('loginFailure', error)
          dispatch('alert/error', error, { root: true })
        }
      )
  },
  logout ({ commit }) {
    userService.logout()
    commit('logout')
  }

}
