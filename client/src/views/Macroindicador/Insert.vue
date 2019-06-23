<template>
<div>
    <v-stepper v-model="el" class="container fluid insert-stepper" >
      <v-stepper-header>
        <v-stepper-step :complete="el > 1" step="1">Importar os dados</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="el > 2" step="2">Confira os Indicadores</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">Criar Visão</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <v-layout row justify-end>
            <v-flex xs2>
              <v-btn
                color="amber darken-4"
                @click="sendForm()"
              >
                Continuar
               </v-btn>
             </v-flex>
           </v-layout>          
          <initial-form ref="iniForm"
            :idMacroindicador="idMacroindicador"
            v-on:update:id-macroindicador="idMacroindicador = $event"
          />
        
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-layout row justify-end>
            <v-flex xs2>              
              <v-btn
                color="amber darken-4"
                @click="nextStep"
              >
                Continuar
              </v-btn>
             </v-flex>
           </v-layout>         
          <tree-fields :idMacroindicador="idMacroindicador"/>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
        <v-stepper-content step="3">
          <v-layout row justify-end>
            <v-flex xs2>              
              <v-btn color="amber darken-4" style="margin-left: -70px;" @click="salvarVisao()">
                Salvar Visão e Finalizar
              </v-btn>
             </v-flex>
           </v-layout>

          <create-view
            ref="createview"
            :idMacroindicador="idMacroindicador"
          />
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
   
  </div>
</template>

<script>
import InitialForm from '@/components/Macroindicador/InitialForm'
import TreeFields from '@/components/Macroindicador/TreeFields'
import CreateView from '@/components/Macroindicador/CreateView'
import { mapActions, mapMutations } from 'vuex'

export default {
  components: {
    'initial-form': InitialForm,
    'tree-fields': TreeFields,
    'create-view': CreateView
  },
  data () {
    return {      
      idMacroindicador: {},
      
    }
  },
  computed :{
    
    el: {       
      get: function () {
        return this.$store.state.formsteps.formProgress
      },      
      set: function (newValue) {        
      }
      
    }
  },
  watch: {
    idMacroindicador () {
      this.offLoading();
      if (this.idMacroindicador.idMacroindicador)
        this.idMacroindicador = this.idMacroindicador.idMacroindicador
    }
  },
  methods: {
    ...mapActions('formsteps', ['nextStep', 'reset']),
    ...mapMutations('app', ['onLoading', 'offLoading']),
    sendForm () {
      this.$refs.iniForm.send()      
    },
    salvarVisao () {
      this.$refs.createview.send(this.idMacroindicador);      
      this.onLoading()      
    }
  },
  mounted () {
    this.reset()
    this.$store.subscribe((mutation, state) => {
      switch(mutation.type) {
        case 'visao/updateVisao':
          this.$router.push({ path: `/macroindicadores` });
          this.offLoading();
          break;
      }
    })
  }
}

</script>

<style scoped>
  .insert-stepper {
    height: 100%;
  }
</style>
