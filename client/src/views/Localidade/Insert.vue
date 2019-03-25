<template>
    <v-stepper v-model="el" class="container fluid insert-stepper" >
      <v-stepper-header>
        <v-stepper-step :complete="el > 1" step="1">Inicio</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="el > 2" step="2">Hierarquia de Indicadores</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">Inserir dados</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <initial-form ref="iniForm" />

          <v-btn
            color="amber darken-4"
            @click="el = sendForm()"
          >
            Continue
          </v-btn>

          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">

          <tree-fields :idMacroindicador="idMacroindicador" />

          <v-btn
            color="amber darken-4"
            @click="el = 3"
          >
            Continue
          </v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
        <v-stepper-content step="3">
          <v-card
            class="mb-5"
            color="grey lighten-1"
            height="200px"
          ></v-card>
          <v-btn color="amber darken-4" @click="el = 1">
            Continue
          </v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
</template>

<script>
import InitialForm from '@/components/Macroindicador/InitialForm'

import TreeFields from '@/components/Macroindicador/TreeFields'

export default {
  components: {
    'initial-form': InitialForm,
    'tree-fields': TreeFields
  },
  data () {
    return {
      el: 0,
      idMacroindicador: ''
    }
  },
  methods: {
    sendForm () {
      this.$refs.iniForm.send()
      return 2
    }
  }
}

</script>

<style scoped>
  .insert-stepper {
    height: 100%;
  }
</style>
