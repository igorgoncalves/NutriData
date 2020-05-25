<template>
  <div>
    <v-container>
      <categoria-form :categoria="categoria" />
    </v-container>
  </div>
</template>

<script>
import CategoriaForm from "@/components/Categorias/CategoriaForm";
import { mapActions, mapState } from "vuex";

export default {
  components: {
    "categoria-form": CategoriaForm,
  },
  computed: {
    ...mapState("categorias", ["categoria"]),
  },
  methods: {
    ...mapActions("categorias", ["fetchCategoria"]),
  },
  mounted() {
    let idCategoria = this.$route.params.idCategoria;
    this.fetchCategoria(idCategoria);
  },
};
</script>

<style scoped>
.insert-stepper {
  height: 100%;
}
</style>
