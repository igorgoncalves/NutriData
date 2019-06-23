<template>
<div>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"      
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

  <v-btn
      color="error"
      @click="reset"
    >
      Limpar
    </v-btn>

  <v-dialog
      v-model="dialogOps"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Ops! Encontramos alguns problemas</v-card-title>

        <v-card-text>
          <p> Acreditamos que sua planilha tem alguns problemas de formatação, acesse o link para abaixar o arquivo comentado</p>
          <v-spacer></v-spacer>
       
          <a :href="dialogLink" target="_blank"> Baixar arquivo</a>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>          

          <v-btn
            color="green darken-1"
            flat="flat"
            @click="dialogOps = false"
          >
            Entendi!
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</div>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { mapActions, mapMutations } from 'vuex'

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
    dropzoneOptions: {
      url: '/api/macroindicadores',
      thumbnailWidth: 150,
      maxFilesize: 0.5,
      maxFiles: 1,
      autoProcessQueue: false
    },
    dialogOps: false,
    dialogLink: ""
  }),

  methods: {
    ...mapActions('indicadores', ['getIndicadoresById']),
    ...mapActions('macroindicadores', ['fetchMacroindicadores']),
    ...mapActions('formsteps', ['nextStep']),
    ...mapMutations('app', ['onLoading', 'offLoading']),
    validate () {
      if (this.$refs.form.validate()) {
        this.snackbar = true
      }
    },
    reset () {
      this.$refs.form.reset();
      this.$refs.myVueDropzone.removeAllFiles()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
    updateIndicadores (response) {      
      
      response = JSON.parse(response.xhr.response);
      let data = JSON.parse(response.data);
      
      if (response.detail !== "") {        
        this.$refs.myVueDropzone.removeAllFiles();
        this.dialogLink = "/" + response.detail;
        this.dialogOps = true;
        this.offLoading();
        return 
      }      
            
      this.$emit('update:id-macroindicador', data.id);
      this.nextStep()
    },
    send () {
      if (this.$refs.form.validate() &&
          this.$refs.myVueDropzone.getQueuedFiles().length > 0){                
        
        this.onLoading();
        this.$refs.myVueDropzone.processQueue()
        
      } else {
        alert("Confira os campos do formulário antes de enviar")
      }
    },
    addParams (file, xhr, formData) {
      formData.append('nome', this.name);
      formData.append('descricao', this.description);
      formData.append('codigoLocalidade', this.$route.params.codigoLocalidade)
    },
  },
  mounted () {
    this.$store.subscribe((mutation, state) => {
      switch(mutation.type) {
        case 'indicadores/updateIndicadores':
          
      }
    })
  }
  
}
</script>

<style scoped>

</style>
