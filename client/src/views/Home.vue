<template>
  <div>
    <h1> Código: {{ localidade }}</h1>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
     <v-flex xs5>
        <map-select v-model="localidade" />
      </v-flex>
      <v-flex xs7>
        <v-layout row wrap>
          <v-flex xs4 v-for="(indicador, index) in indicadores" :key="index">
          <v-card class="card-indicador" min-height="100px">
            <v-card-text>{{ indicador.text }}</v-card-text>
          </v-card>
          </v-flex>
        </v-layout>
      </v-flex>
       </v-layout>
  </v-container>

  </div>
</template>

<script>

import MapSelect from '@/components/Home/MapSelect'

export default {
  components: {
    'map-select': MapSelect
  },
  data () {
    return {
      localidade: 0
    }
  },
  computed: {
    indicadores () {
      // return this.$store.getters.getIndicadores
    }
  },
  watch: {
    localidade: function () {
      // this.$store.dispatch('getIndicadoresByLocalidade', { idLocalidade: this.localidade })
    }
  },
  mounted () {
    // this.$store.dispatch('initIndicadores')
  }
}

</script>

<style scoped>
  .card-indicador{
    background:#27ae60;
    text-align: left;
    color: white;
    font-weight: 700;

  }
</style>
