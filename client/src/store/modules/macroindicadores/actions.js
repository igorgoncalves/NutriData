import Vue from "vue";

// https://vuex.vuejs.org/en/actions.html
export default {
  initMacroindicadores(context) {
    context.commit("initMacroindicadores");
  },

  fetchMacroindicadores(context) {
    Vue.prototype.$http
      .get(`/api/macroindicadores`)
      .then((response) => {
        context.commit("updateMacroindicadores", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  fetchMacroindicadoresByLocalidade(context, codigoLocalidade) {
    Vue.prototype.$http
      .get(`/api/localidade/${codigoLocalidade}/macroindicadores`)
      .then((response) => {
        context.commit("updateMacroindicadores", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  fetchMacroindicadoresById(context, idMacroindicador) {
    Vue.prototype.$http
      .get(`/api/macroindicadores/${idMacroindicador}`)
      .then((response) => {
        context.commit("updateMacroindicador", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  fetchMacroindicadoresByIdandLocaliade(
    context,
    { codigoLocalidade, idMacroindicador }
  ) {
    Vue.prototype.$http
      .get(
        `/api/localidade/${codigoLocalidade}/macroindicadores/${idMacroindicador}`
      )
      .then((response) => {
        context.commit("updateMacroindicador", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  deleteMacroindicador(context, idMacroindicador) {
    Vue.prototype.$http
      .delete(`/api/macroindicadores/${idMacroindicador}`)
      .then((response) => {
        context.commit("deleteMacroindicador", idMacroindicador);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  updateMacroindicador(context, { idMacroindicador, nome, descricao }) {
    Vue.prototype.$http
      .patch(`/api/macroindicadores/${idMacroindicador}`,  { nome, descricao })
      .then((response) => {
        console.log(response.data);
        
        context.commit("updateMacroindicador", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
