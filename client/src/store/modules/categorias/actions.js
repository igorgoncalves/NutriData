import Vue from "vue";

// https://vuex.vuejs.org/en/actions.html
export default {
  fetchCategorias(context) {
    Vue.prototype.$http
      .get(`/api/categorias`)
      .then((response) => {
        context.commit("UPDATE_CATEGORIAS", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  fetchCategoria(context, id) {
    Vue.prototype.$http
      .get(`/api/categorias/${id}`)
      .then((response) => {
        context.commit("UPDATE_CATEGORIA", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  createCategoria(context, { nome, descricao }) {
    Vue.prototype.$http
      .post(`/api/categorias`, { nome, descricao })
      .then((response) => {
        console.log(response.data);
        context.commit("UPDATE_CATEGORIA", response.data);
        context.dispatch("fetchCategorias");
      })
      .catch((error) => {
        console.error(error);
      });
  },
  deleteCategoria(context, id) {
    Vue.prototype.$http
      .delete(`/api/categorias/${id}`)
      .then((_) => {
        context.commit("UPDATE_CATEGORIA", null);
        context.dispatch("fetchCategorias");
      })
      .catch((error) => {
        console.error(error);
      });
  },
  updateCategoria(context, { id, nome, descricao }) {
    Vue.prototype.$http
      .patch(`/api/categorias/${id}`, { nome, descricao })
      .then((response) => {
        console.log(response.data);
        context.commit("UPDATE_CATEGORIA", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
