import { userService } from '../../../services'
// https://vuex.vuejs.org/en/actions.html

export default {
  getAll ({ commit }) {
    commit('getAllRequest')

    userService.getAll()
      .then(
        users => commit('getAllSuccess', users),
        error => commit('getAllFailure', error)
      )
  }

}
