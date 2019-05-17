<template>
  <div>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
      <v-flex
        md12
        sm12
        lg6
      >
        <v-autocomplete          
          :items="getLocalidadeNomes"          
          item-text="name"
          label="Localidade"
          v-model="nome"
        ></v-autocomplete>        

        <h2>1º - Selecione o local</h2>
        <map-select v-model="localidade" />
      </v-flex>
      <v-flex xs1>
      <v-divider hidden-md-and-down vertical></v-divider>
      </v-flex>
      <v-flex
        md12
        sm12
        lg5
      >
        <div>
          <h2>2º - Clique em um indicador de: {{ nomeLocalidade }}</h2>
          <v-layout row wrap>
            <transition-group name="fade" tag="div" class="layout row wrap">
            <v-flex lg4 md6 v-for="indicador in macroindicadores" :key="indicador.nome + componentKey + Math.random()" >
               <v-hover>
                  <v-card
                    slot-scope="{ hover }"
                    :class="`elevation-${hover ? 12 : 2}`"
                    class="mx-auto card-indicador"
                    color="success" min-height="100px" @click="showVisao(indicador.id)"
                  >                
                  <v-card-text> {{ indicador.nome }} </v-card-text>
                  </v-card>
              </v-hover>
            </v-flex>
            </transition-group>
          </v-layout>
        </div>
      </v-flex>
      
      <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">      
      <v-card>
        <v-btn                     
          class="close"
          @click="dialog = false">
          Voltar            
          </v-btn>        
        <show-graph id='chart-panel' ref="chart" />
      </v-card>
    </v-dialog>                                
      
       </v-layout>
  </v-container>

  </div>
</template>

<script>

import MapSelect from '@/components/Home/MapSelect'
import ShowGraph from '@/components/Home/ShowGraph'
import goTo from 'vuetify/lib/components/Vuetify/goTo'

import { mapGetters, mapActions } from 'vuex'

export default {
  components: {
    'map-select': MapSelect,
    'show-graph': ShowGraph
  },
  data () {
    return {
      localidade: 0,
      componentKey: 0,
      showChart: true,
      nome: '',
      dialog: false
    }
  },
  computed: {
    ...mapGetters('macroindicadores', ['getMacroindicadores']),
    ...mapGetters('localidades', ['getLocalidadeName', 'getLocalidadeNomes', 'getCodigoLocalidadePorNome']),
    macroindicadores () {
      return this.getMacroindicadores
    },
    nomeLocalidade () {
      return this.getLocalidadeName(this.localidade)
    }
  },
  watch: {
    nome: function (nomeSelecionado) {
      this.localidade = this.getCodigoLocalidadePorNome(nomeSelecionado)
    },
    localidade: function () {
      this.fetchMacroindicadoresByLocalidade(this.localidade)
    }
  },  
  methods:{
    ...mapActions('macroindicadores', ['fetchMacroindicadoresByLocalidade']),
    ...mapActions('localidades', ['fetchLocalidades']),    
    showVisao (idMacroindicador) {
      this.$refs.chart.loadChart(idMacroindicador, this.localidade)
      this.dialog = true
      // this.$vuetify.goTo('#chart-panel')
    }
  } ,
  mounted () {
    this.fetchMacroindicadoresByLocalidade(this.localidade)
    this.fetchLocalidades()
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
  .fade-enter-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  .close {
    background:#16a085 !important;
    float: right;
    margin-right: 40px;
  }

</style>
