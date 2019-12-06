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
// import TreeFields from "@/components/Macroindicador/TreeFields";
// import CreateView from "@/components/Macroindicador/CreateView";
import { mapActions, mapMutations } from "vuex";

export default {
  components: {
    "initial-form": InitialForm,
    // "tree-fields": TreeFields,
    // "create-view": CreateView
  },
  data() {
    return {
      idMacroindicador: {}
    };
  },
  computed: {
    el: {
      get: function() {
        return this.$store.state.formsteps.formProgress;
      },
      set: function(newValue) {}
    }
  },
  watch: {
    idMacroindicador() {
      this.offLoading();
      if (this.idMacroindicador.idMacroindicador)
        this.idMacroindicador = this.idMacroindicador.idMacroindicador;
    }
  },
  methods: {
    ...mapActions("formsteps", ["nextStep", "reset"]),
    ...mapMutations("app", ["onLoading", "offLoading"]),
    sendForm() {
      this.$refs.iniForm.send();
    },
    salvarVisao() {
      this.$router.push({ path: `/macroindicadores` });
    }
  }
};
</script>

<style scoped>
.insert-stepper {
  height: 100%;
}
</style>
