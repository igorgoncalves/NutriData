// https://vuex.vuejs.org/en/getters.html

export default {
  nomesDasCategorias: (state) => {
    console.log(state.categorias);
    
    return state.categorias
  },
};
