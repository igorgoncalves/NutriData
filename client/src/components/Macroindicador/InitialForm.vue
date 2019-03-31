<template>
<div>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Nome"
      required
    ></v-text-field>

    <v-text-field
      v-model="description"
      :rules="descriptionRules"
      label="Descricao"
      required
    ></v-text-field>

    <!-- <v-btn
      :disabled="!valid"
      color="success"
      @click="validate"
    >
      Validate
    </v-btn> -->
<!--
    <v-btn
      color="error"
      @click="reset"
    >
      Limpar
    </v-btn> -->

    <!-- <v-btn
      color="warning"
      @click="resetValidation"
    >
      Reset Validation
    </v-btn> -->
  </v-form>

  <h3>Enviar arquivo</h3>
  <vue-dropzone
    id="dropzone"
    ref="myVueDropzone"
    v-on:vdropzone-complete.passive="updateIndicadores"
    v-on:vdropzone-sending="addParams"
    :options="dropzoneOptions"
    :useCustomSlot=true>
    <div class="dropzone-custom-content">
      <h3 class="dropzone-custom-title">Arraste a arquivo da planilha para dentro dessa área</h3>
    <div class="subtitle">...ou clique e selecione o arquivo</div>
    </div>
  </vue-dropzone>

</div>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { mapActions } from 'vuex'

export default {
  components: {
    'vue-dropzone': vue2Dropzone
  },

  data: () => ({
    valid: true,
    name: '',
    nameRules: [
      v => !!v || 'Por favor, é necessŕio que preeencha o campo nome'
    ],
    description: '',
    descriptionRules: [
      v => !!v || 'Por favor, é necessŕio que preeencha o campo descrição'
    ],
    select: null,
    items: [
      'Item 1',
      'Item 2',
      'Item 3',
      'Item 4'
    ],
    checkbox: false,
    dropzoneOptions: {
      url: '/api/macroindicadores',
      thumbnailWidth: 150,
      maxFilesize: 0.5,
      maxFiles: 1,
      autoProcessQueue: false
    }
  }),

  methods: {
    ...mapActions('indicadores', ['getIndicadoresById']),
    ...mapActions('macroindicadores', ['fetchMacroindicadores']),
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
    updateIndicadores (response) {
      let idMacroindicador = JSON.parse(response.xhr.response).id
      this.$emit('update:id-macroindicador', idMacroindicador)
      this.getIndicadoresById(idMacroindicador)
    },
    send () {
      this.$refs.myVueDropzone.processQueue()
    },
    addParams (file, xhr, formData) {
      formData.append('nome', this.name)
      formData.append('descricao', this.description)
      formData.append('codigoLocalidade', this.$route.params.codigoLocalidade)
    },
  }
}
</script>

<style scoped>

</style>
