<template>
    <v-stepper v-model="e1" class="container fluid insert-stepper" >
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" step="1">Inicio</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="e1 > 2" step="2">Hierarquia de Indicadores</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">Inserir dados</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <initial-form />

          <v-btn
            color="primary"
            @click="e1 = 2"
          >
            Continue
          </v-btn>

          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">

          <tree-fields :idMacroindicador="1" />

          <v-btn
            color="primary"
            @click="e1 = 3"
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
          <v-btn color="primary" @click="e1 = 1">
            Continue
          </v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
</template>

<script>
import InitialForm from './subcomponents/InitialForm'

import TreeFields from './subcomponents/TreeFields'

export default {
  components: {
    'initial-form': InitialForm,
    'tree-fields': TreeFields
  },
  data () {
    return {
      e1: 0
    }
  }
}

</script>

<style scoped>
  .insert-stepper {
    height: 100%;
  }
</style>
