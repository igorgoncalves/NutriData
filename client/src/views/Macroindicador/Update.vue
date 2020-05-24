<template>
  <div>
    <v-container>
      <initial-form
        ref="iniForm"
        :macroindicador="macroindicador"
        v-on:update:id-macroindicador="idMacroindicador = $event"
      />
    </v-container>
  </div>
</template>

<script>
import InitialForm from "@/components/Macroindicador/InitialForm";
import { mapActions, mapState } from "vuex";

export default {
  components: {
    "initial-form": InitialForm,
  },  
  computed: {
    ...mapState("macroindicadores", ["macroindicador"]),
  },
  methods: {
    ...mapActions("macroindicadores", ["fetchMacroindicadoresById"]),
  },  
  mounted() {
    let idMacroindicador = this.$route.params.idMacroindicador;
    this.fetchMacroindicadoresById(idMacroindicador);
  },
};
</script>

<style scoped>
.insert-stepper {
  height: 100%;
}
</style>
