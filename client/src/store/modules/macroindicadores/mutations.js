// https://vuex.vuejs.org/en/mutations.html

import Macroindicador from "../../../models/macroindicador";

export default {
  initMacroindicadores(state, payload) {
    state.macroindicadores = payload;
  },
  updateMacroindicadores(state, payload) {
    state.macroindicadores = payload.map(macroindicador => {      
      return new Macroindicador({ ...macroindicador });
    });
  },
  updateMacroindicador(state, payload) {
    state.macroindicador = new Macroindicador({ ...payload });
  },
  deleteMacroindicador(state, idMacroindicador) {
    state.macroindicadores = state.macroindicadores.filter(macroindicador => {
      return macroindicador.id != idMacroindicador;
    });
  }
};
