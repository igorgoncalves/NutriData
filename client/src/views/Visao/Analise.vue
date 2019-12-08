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
      <v-flex
        md12
        sm12
        lg4>
        <v-card>
          <v-flex
            md12
            sm12
            lg12>
            <v-btn
                color="success"
                @click="updateChart()"
              >Atualizar gráfico</v-btn>
          </v-flex>
          <v-flex
            md12
            sm12
            lg12>
              <v-select
                  :items="form[0].options"
                  :label="form[0].label"
                  v-model="form[0].value"
                  v-on:change="changeChart()"
                  outline
              ></v-select>
            </v-flex>
        <v-list
            subheader
            two-line
          >
            <v-subheader>Indicadores</v-subheader>
            <v-list-tile v-for="(indicador, key) in filteredMacroindicador.indicadores"  :key="key">
              <v-list-tile-action>
                <v-checkbox v-model="filteredMacroindicador.indicadores[key].value" ></v-checkbox>
              </v-list-tile-action>
              <v-list-tile-content @click="filteredMacroindicador.indicadores[key].value = !filteredMacroindicador.indicadores[key]">
                <v-list-tile-title>{{ indicador.nome }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
          </v-card>
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
import pie from './pie'
import bar from './bar'
import line from './line'
import form from './form'

export default {
  components: {
    'v-chart': ECharts
  },
  computed: {
    ...mapGetters('macroindicadores', ['getMacroindicadorById']),
    filteredMacroindicador() {
      return this.getMacroindicadorById(this.$route.params.idMacroindicador)
    }
  },
  data() {
    return {
      pie: pie,
      bar: bar,
      line: line,
      form,
      indicadores: [],
      chart: {},
      type: ""
    }
  },
  methods: {
    changeChart() {
      switch (this.form[0].value) {
        case "Pizza":
          this.chart = this.pie;
          this.type = "pie";
          break;
        case "Barra":
          this.chart = this.bar;
          this.type = "bar";
          break;
        case "Linha":
          this.chart = this.line;
          this.type = "line";
          break;
        default:
          this.chart = {};
          break;
      }
      this.updateChart()
    },
    checkIndicador(valor) {
      this.updateChart();
      return valor
    },
    updateChart(){
      let indicadores = this.filteredMacroindicador.indicadores.filter(el => {
        return el.value && el.value != false
      });

      var retorno = [];
      switch (this.type) {
        case 'pie':
          retorno = indicadores.map((indicador) => {
            return {
              name: indicador.nome,
              value: indicador.amostras.filter(am => am.codigoLocalidade == 0).map((el) => el)[0].valor
            }
          });
          this.chart.series[0].data = retorno;
          this.chart.series[0].name = this.filteredMacroindicador.unidade;
          this.chart.legend.data = indicadores.map(el => el.nome);
          break;
        case 'line':
        case 'bar':
          retorno = indicadores.map((indicador) => {
            return {
              type: this.type,
              name: indicador.nome,
              data: indicador.amostras.filter(am => am.codigoLocalidade == 0).map(am => am.valor)
            }
          });
          this.chart.xAxis = {
            type: 'category',
            boundaryGap: false,
            data: indicadores[0].amostras.filter(am => am.codigoLocalidade == 0).map((am) => am.ano)
          };
          this.chart.series = retorno;
          break;
      }
      this.$refs.chart.clear();
      this.$refs.chart.mergeOptions(this.chart)
    }
  }
}

</script>

<style>
.echarts {
  width: 100% !important;
}
</style>
