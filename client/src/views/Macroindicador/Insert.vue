<template>
  <div>
    <v-container>
    <initial-form
      ref="iniForm"
      :idMacroindicador="idMacroindicador"
      v-on:update:id-macroindicador="idMacroindicador = $event"
    />
    </v-container>
  </div>
</template>

<script>
import InitialForm from "@/components/Macroindicador/InitialForm";
import { mapActions, mapMutations } from "vuex";

export default {
  components: {
    "initial-form": InitialForm,
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
