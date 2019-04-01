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
        lg12>
        <v-flex
        md12
        sm12
        lg12>
          <h2> {{ macroindicador.nome }} </h2>
          <span>{{ macroindicador.descricao }}</span>
        </v-flex>
        <v-flex
          md12
          sm12
          lg12>
          <v-chart
            :options="chart"
            ref="chart"
            autoresize
          />
        </v-flex>
        <v-flex
        md12
        sm12
        lg12>
          <p> {{ macroindicador.fonte }} </p>
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
    ...mapGetters('macroindicadores', ['getMacroindicadorAndVisao']),
    macroindicador() {
      return this.getMacroindicadorAndVisao
    }
  },
  data() {
    return {
      pie: pie,
      bar: bar,
      line: line,
      indicadores: [],
      chart: {},
      type: "",
      idLocalidade: 0
    }
  },
  methods: {
    ...mapActions('macroindicadores', ['fetchMacroindicadoresById']),
    loadChart (idMacroindicador, idLocalidade) {
      this.idLocalidade = idLocalidade
      this.fetchMacroindicadoresById(idMacroindicador)
    },
    updateChart (idLocalidade) {
      let indicadores = this.macroindicador.visao.indicadores
      this.chart = eval(`this.${this.macroindicador.visao.tipo_do_grafico}`);
      var retorno = []
      switch (this.macroindicador.visao.tipo_do_grafico) {
        case 'pie':
          retorno = indicadores.map((indicador) => {
            return {
              name: indicador.nome,
              value: indicador.amostras.filter(am => am.codigo_localidade == idLocalidade).map((el) => el)[0].valor
            }
          })
          this.chart.series[0].data = retorno
          this.chart.series[0].name = this.macroindicador.unidade
          this.chart.legend.data = indicadores.map(el => el.nome)
          break;
        case 'line':
        case 'bar':
          retorno = indicadores.map((indicador) => {
            return {
              type: this.macroindicador.visao.tipo_do_grafico,
              name: indicador.nome,
              data: indicador.amostras.filter(am => am.codigo_localidade == idLocalidade).map(am => am.valor)
            }
          })
          this.chart.xAxis = {
            type: 'category',
            boundaryGap: false,
            data: indicadores[0].amostras.filter(am => am.codigo_localidade == idLocalidade).map((am) => am.ano)
          }

          this.chart.series = retorno
          break;
      }
      this.$refs.chart.clear()
      this.$refs.chart.mergeOptions(this.chart)
    }
  },
  mounted () {
    this.$store.subscribe((mutation, state) => {
      switch(mutation.type) {
        case 'macroindicadores/updateMacroindicador':
          this.updateChart(this.idLocalidade)
          break;
      }
    })
  }
}

</script>

<style>
.echarts {
  width: 100vw !important;
  max-height: 100vw !important;

}

.lista-indicadores{
    overflow-y: scroll;
    height: 100vh;
}
</style>
