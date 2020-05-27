<template>
  <div>
    <h2>Cadastro de novos indicadores</h2>
    <small
      >O cadastro de novos indicadores é feito por meio do envio de uma planilha
      com os dados dos macroindicadores</small
    >
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="name"
        :rules="nameRules"
        label="Nome"
        required
      ></v-text-field>

      <v-select
        :items="nomesDasCategorias"
        label="Categoria"
        item-text="nome"
        item-value="nome"
        v-model="categoria"
      ></v-select>      

      <h5>Descrição do macro indicador</h5>
      <tiptap-vuetify
        v-model="description"
        :extensions="extensions"
        :toolbar-attributes="{ color: '#47a14b' }"
      />
    </v-form>
    <div v-if="isNew">
      <h3>Enviar arquivo</h3>
      <vue-dropzone
        id="dropzone"
        ref="myVueDropzone"
        v-on:vdropzone-complete.passive="updateIndicadores"
        v-on:vdropzone-sending="addParams"
        :options="dropzoneOptions"
        :useCustomSlot="true"
      >
        <div class="dropzone-custom-content">
          <h3 class="dropzone-custom-title">
            Arraste a arquivo da planilha para dentro dessa área
          </h3>
          <div class="subtitle">...ou clique e selecione o arquivo</div>
        </div>
      </vue-dropzone>
      <div style="float: right;">
        <v-btn color="error" @click="reset">Limpar</v-btn>
        <v-btn color="green darken-2" @click="send()">Salvar</v-btn>
      </div>

      <v-dialog v-model="dialogOps" max-width="290">
        <v-card>
          <v-card-title class="headline"
            >Ops! Encontramos alguns problemas</v-card-title
          >

          <v-card-text>
            <p>
              Acreditamos que sua planilha tem alguns problemas de formatação,
              acesse o link para abaixar o arquivo comentado
            </p>
            <v-spacer></v-spacer>

            <a :href="dialogLink" target="_blank">Baixar arquivo</a>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="green darken-1" flat="flat" @click="dialogOps = false"
              >Entendi!</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
    <div v-if="!isNew" style="float: right;">
      <v-btn color="green darken-2" @click="update()">Atualizar</v-btn>
    </div>
  </div>
</template>

<script>
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.min.css";
import {
  TiptapVuetify,
  Heading,
  Bold,
  Italic,
  Strike,
  Underline,
  Code,
  CodeBlock,
  Paragraph,
  BulletList,
  OrderedList,
  ListItem,
  Link,
  Blockquote,
  HardBreak,
  HorizontalRule,
  History,
} from "tiptap-vuetify";

import { mapActions, mapMutations, mapState, mapGetters } from "vuex";

export default {
  props: ["macroindicador"],
  components: {
    "vue-dropzone": vue2Dropzone,
    TiptapVuetify,
  },

  data: () => ({
    extensions: [
      // you can specify options for extension
      new Heading({
        levels: [1, 2, 3],
      }),
      new Bold(),
      new Italic(),
      new Strike(),
      new Underline(),
      new Code(),
      new CodeBlock(),
      new Paragraph(),
      new BulletList(),
      new OrderedList(),
      new ListItem(),
      // new Link(),
      new Blockquote(),
      new HardBreak(),
      new HorizontalRule(),
      new History(),
    ],
    // starting editor's content
    content: "",
    valid: true,
    name: "",
    nameRules: [
      (v) => !!v || "Por favor, é necessŕio que preeencha o campo nome",
    ],
    categoria: "",
    categoriaRules: [
      (v) => !!v || "Por favor, é necessŕio que preeencha o campo categoria",
    ],
    description: "",
    descriptionRules: [
      (v) => !!v || "Por favor, é necessŕio que preeencha o campo descrição",
    ],
    dropzoneOptions: {
      url: "/api/macroindicadores",
      thumbnailWidth: 150,
      maxFilesize: 0.5,
      maxFiles: 1,
      autoProcessQueue: false,
    },
    dialogOps: false,
    dialogLink: "",
  }),

  computed: {
    isNew() {
      return !this.macroindicador;
    },
    ...mapGetters("categorias", ["nomesDasCategorias"]),
  },
  methods: {
    ...mapActions("indicadores", ["getIndicadoresById"]),
    ...mapActions("categorias", ["fetchCategorias"]),
    ...mapActions("macroindicadores", [
      "fetchMacroindicadores",
      "updateMacroindicador",
    ]),
    ...mapActions("formsteps", ["nextStep"]),
    ...mapMutations("app", ["onLoading", "offLoading"]),
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.description = "";
      this.$refs.form.reset();
      this.$refs.myVueDropzone.removeAllFiles();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    updateIndicadores(response) {
      response = JSON.parse(response.xhr.response);
      let data = JSON.parse(response.data);

      if (response.detail !== "") {
        this.$refs.myVueDropzone.removeAllFiles();
        this.dialogLink = "/" + response.detail;
        this.dialogOps = true;
        this.offLoading();
        return;
      }

      this.$emit("update:id-macroindicador", data.id);
      this.nextStep();
    },
    send() {
      if (
        this.$refs.form.validate() &&
        this.$refs.myVueDropzone.getQueuedFiles().length > 0
      ) {
        this.$refs.myVueDropzone.processQueue();
        // this.reset();
      } else {
        alert("Confira os campos do formulário antes de enviar");
      }
    },
    addParams(file, xhr, formData) {
      formData.append("nome", this.name);
      formData.append("categoria", this.categoria);
      formData.append("descricao", this.description);
      formData.append("codigoLocalidade", this.$route.params.codigoLocalidade);
    },
    async update() {
      await this.updateMacroindicador({
        idMacroindicador: this.macroindicador.id,
        nome: this.name,
        descricao: this.description,
      });
      this.$router.push({ path: `/macroindicadores` });
    },
  },
  watch: {
    macroindicador: function() {
      console.log(this.macroindicador)
      this.name = this.macroindicador.nome;
      this.description = this.macroindicador.descricao;
      this.categoria = this.macroindicador.categoria;
    },
  },
  mounted() {
    this.fetchCategorias();
    this.$store.subscribe((mutation, state) => {
      switch (mutation.type) {
        case "indicadores/updateIndicadores":
      }
    });
  },
  beforeDestroy() {
    // this.editor.destroy();
  },
};
</script>

<style scoped></style>
