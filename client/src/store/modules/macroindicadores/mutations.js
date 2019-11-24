// https://vuex.vuejs.org/en/mutations.html

export default {
  initMacroindicadores(state, payload) {
    state.macroindicadores = payload;
  },
  updateMacroindicadores(state, payload) {
    state.macroindicadores = payload;
  },
  updateMacroindicador(state, payload) {
    state.macroindicador = payload;
  },
  deleteMacroindicador(state, idMacroindicador) {
    state.macroindicadores = state.macroindicadores.filter(macroindicador => {
      return macroindicador.id != idMacroindicador;
    });
  }
};
