<template>
  <div>        
    <create-view ref="createview" :idMacroindicador="idMacroindicador" :idLocalidade="codigoLocalidade" />
  </div>
</template>

<script>
import CreateView from "@/components/Macroindicador/CreateView";
import { mapActions, mapMutations } from "vuex";

export default {
  components: {
    "create-view": CreateView
  },
  data() {
    return {};
  },
  computed: {
    idMacroindicador() {
      return this.$route.params.idMacroindicador;
    },
    codigoLocalidade() {
      return this.$route.params.codigoLocalidade;
    }
  },
  methods: {
    ...mapActions("macroindicadores", [
      "fetchMacroindicadoresByLocalidade",
      "fetchMacroindicadoresByIdandLocaliade"
    ]),
    ...mapActions("localidades", ["fetchLocalidades"]),
  },
  mounted() {        
    this.fetchLocalidades();
    this.fetchMacroindicadoresByIdandLocaliade({
      codigoLocalidade: this.codigoLocalidade,
      idMacroindicador: this.idMacroindicador
    });
  }
};
</script>

<style>
</style>