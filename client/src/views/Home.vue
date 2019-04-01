<template>
  <div>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
      <v-flex xs5>
        <h1>Selecione o local</h1>
        <map-select v-model="localidade" />
      </v-flex>
      <v-flex xs1>
      <v-divider vertical></v-divider>
      </v-flex>
      <v-flex xs6>
        <h2>Indicadores de: Brasil</h2>
        <v-layout row wrap>
          <v-flex xs4 v-for="(indicador, index) in macroindicadores" :key="index">
          <v-card :color="success" class="card-indicador" min-height="100px">
            <v-card-text>{{ indicador.nome }}</v-card-text>
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
import { mapGetters, mapActions } from 'vuex'

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
    ...mapGetters('macroindicadores', ['getMacroindicadores']),
    macroindicadores () {
      console.log("aqui vai")
      return this.getMacroindicadores
    }
  },
  watch: {
    localidade: function () {
      this.fetchMacroindicadoresByLocalidade(this.localidade)
    }
  },
  methods:{
    ...mapActions('macroindicadores', ['fetchMacroindicadoresByLocalidade']),
  } ,
  mounted () {
    this.fetchMacroindicadoresByLocalidade(this.localidade)
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
