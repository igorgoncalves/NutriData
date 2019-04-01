<template>
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
          <initial-form ref="iniForm"
            :idMacroindicador="idMacroindicador"
            v-on:update:id-macroindicador="idMacroindicador = $event"
          />

          <v-btn
            color="amber darken-4"
            @click="el = sendForm()"
          >
            Continuar
          </v-btn>

          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">

          <tree-fields :idMacroindicador="idMacroindicador"/>

          <v-btn
            color="amber darken-4"
            @click="el = 3"
          >
            Continuar
          </v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
        <v-stepper-content step="3">

          <create-view
            ref="createview"
            :idMacroindicador="idMacroindicador"
          />

          <v-btn color="amber darken-4" @click="salvarVisao()">
            Salvar Visão e Finalizar
          </v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
</template>

<script>
import InitialForm from '@/components/Macroindicador/InitialForm'
import TreeFields from '@/components/Macroindicador/TreeFields'
import CreateView from '@/components/Macroindicador/CreateView'

export default {
  components: {
    'initial-form': InitialForm,
    'tree-fields': TreeFields,
    'create-view': CreateView
  },
  data () {
    return {
      el: 0,
      idMacroindicador: ''
    }
  },
  watch: {
    idMacroindicador () {
      if (this.idMacroindicador.idMacroindicador)
        this.idMacroindicador = this.idMacroindicador.idMacroindicador
    }
  },
  methods: {
    sendForm () {
      this.$refs.iniForm.send()
      return 2
    },
    salvarVisao () {
      this.$refs.createview.send(this.idMacroindicador)
    }
  }
}

</script>

<style scoped>
  .insert-stepper {
    height: 100%;
  }
</style>
