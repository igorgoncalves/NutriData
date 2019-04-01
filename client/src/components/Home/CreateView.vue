<template>
    <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex
        md12
        sm12
        lg8>
        <v-flex
        md12
        sm12
        lg12>
          <h2> {{ filteredMacroindicador.nome }} </h2>
          <span>{{ filteredMacroindicador.descricao }}</span>
        </v-flex>
        <v-flex
          md12
          sm12
          lg12>
          <v-chart
            v-if="chart"
            :options="chart"
            ref="chart"
            autoresize
          />
        </v-flex>
        <v-flex
        md12
        sm12
        lg12>
          <p> {{ filteredMacroindicador.fonte }} </p>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import {
  mapGetters,
  mapActions
} from 'vuex'
import ECharts from 'vue-echarts'
import 'echarts/lib/chart/pie'
import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/line'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/legend/ScrollableLegendModel.js'
import 'echarts/lib/component/legend/ScrollableLegendView.js'
import 'echarts/lib/component/legend/scrollableLegendAction.js'

import pie from '../ChartsDefault/pie'
import bar from '../ChartsDefault/bar'
import line from '../ChartsDefault/line'

export default {
  props:['idMacroindicador'],
  components: {
    'v-chart': ECharts
  },
  computed: {
    ...mapGetters('macroindicadores', ['getMacroindicadorById']),
    ...mapGetters('indicadores', ['getIndicadores']),
    filteredMacroindicador() {
      console.log(this.idMacroindicador)
      return this.getMacroindicadorById(this.idMacroindicador)
    }
  },
  data() {
    return {
      pie: pie,
      bar: bar,
      line: line,
      indicadores: [],
      chart: {},
      type: ""
    }
  },
  methods: {
    ...mapActions('indicadores', ['getIndicadoresById']),
    ...mapActions('visao', ['createVisao']),
    checkIndicador(valor) {
      this.updateChart()
      return valor
    },
    updateChart(){
      let indicadores = this.getIndicadores.filter(el => {
        return el.value && el.value != false
      })

      var retorno = []
      switch (this.type) {
        case 'pie':
          retorno = indicadores.map((indicador) => {
            return {
              name: indicador.nome,
              value: indicador.amostras.filter(am => am.codigo_localidade == 0).map((el) => el)[0].valor
            }
          })
          this.chart.series[0].data = retorno
          this.chart.series[0].name = this.filteredMacroindicador.unidade
          this.chart.legend.data = indicadores.map(el => el.nome)
          break;
        case 'line':
        case 'bar':
          retorno = indicadores.map((indicador) => {
            return {
              type: this.type,
              name: indicador.nome,
              data: indicador.amostras.filter(am => am.codigo_localidade == 0).map(am => am.valor)
            }
          })
          this.chart.xAxis = {
            type: 'category',
            boundaryGap: false,
            data: indicadores[0].amostras.filter(am => am.codigo_localidade == 0).map((am) => am.ano)
          }
          this.chart.series = retorno
          break;
      }
      this.$refs.chart.clear()
      this.$refs.chart.mergeOptions(this.chart)
    }
  }
}

</script>

<style>
.echarts {
  width: 100% !important;
}

.lista-indicadores{
    overflow-y: scroll;
    height: 100vh;
}
</style>
