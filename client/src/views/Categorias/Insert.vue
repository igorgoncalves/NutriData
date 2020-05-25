<template>
  <div>
    <v-container>
    <categoria-form
      ref="iniForm"
      :idCategoria="idCategoria"
      v-on:update:id-macroindicador="idMacroindicador = $event"
    />
    </v-container>
  </div>
</template>

<script>
import CategoriaForm from "@/components/Categorias/CategoriaForm";
import { mapActions, mapMutations } from "vuex";

export default {
  components: {
    "categoria-form": CategoriaForm,
  },
  data() {
    return {
      idMacroindicador: {}
    };
  },  
  watch: {
    idMacroindicador() {
      this.offLoading();
      if (this.idMacroindicador.idMacroindicador)
        this.idMacroindicador = this.idMacroindicador.idMacroindicador;
    }
  },  
};
</script>

<style scoped>
.insert-stepper {
  height: 100%;
}
</style>
