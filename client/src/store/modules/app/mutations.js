import { set, toggle } from '@/utils/vuex'

export default {
  setDrawer: set('drawer'),
  setImage: set('image'),
  setColor: set('color'),
  toggleDrawer: toggle('drawer'),
  onLoading: function (state) {
    state.loading = true
  },
  offLoading: function (state) {
    state.loading = false
  }
}
