// https://vuex.vuejs.org/en/mutations.html

export default {  
  UPDATE_CATEGORIAS (state, payload) {    
    state.categorias = payload
  },
  UPDATE_CATEGORIA (state, payload) {    
    state.categoria = payload
  }
}
