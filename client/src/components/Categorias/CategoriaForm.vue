<template>
  <div>
    <h2>Cadastro de novas categorias</h2>
    <small>O cadastro de novas categorias </small>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="name"
        :rules="nameRules"
        label="Nome"
        required
      ></v-text-field>

      <h5>Descrição da categoria</h5>
      <v-text-field
        v-model="description"
        :rules="descriptionRules"
        label="Descrição"
        required
      ></v-text-field>
    </v-form>
    <div v-if="isNew">
      <div style="float: right;">
        <v-btn color="error" @click="reset">Limpar</v-btn>
        <v-btn color="green darken-2" @click="send()">Salvar</v-btn>
      </div>
    </div>
    <div v-if="!isNew" style="float: right;">
      <v-btn color="green darken-2" @click="update()">Atualizar</v-btn>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";

export default {
  props: ["categoria"],
  components: {        
  },

  data: () => ({  
    // starting editor's content
    content: "",
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Por favor, é necessŕio que preeencha o campo nome",
    ],
    description: "",
    descriptionRules: [
      (v) => !!v || "Por favor, é necessŕio que preeencha o campo descrição",
    ],
  }),

  computed: {
    isNew() {
      return !this.categoria;
    },
  },
  methods: {
    ...mapActions("categorias", [
      "fetchCategorias",
      "updateCategoria",
      "createCategoria",
    ]),
    ...mapMutations("app", ["onLoading", "offLoading"]),
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.description = "";
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    send() {
      this.createCategoria({
        nome: this.name,
        descricao: this.description,
      });
      this.$router.push({ path: `/categorias` });
    },
    async update() {
      await this.updateCategoria({
        idCategoria: this.categoria.id,
        nome: this.name,
        descricao: this.description,
      });
      this.$router.push({ path: `/categorias` });
    },
  },
  watch: {
    categoria: function() {      
      this.name = this.categoria.nome;
      this.description = this.categoria.descricao;
    },
  },
};
</script>

<style scoped></style>
