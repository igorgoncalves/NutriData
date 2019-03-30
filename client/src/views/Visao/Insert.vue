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
        <h4>Preview</h4>
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
        lg4>
        <v-card>
        <h4
        lg10
        >Form</h4>
        <v-select
            :items="form[0].options"
            :label="form[0].label"
            v-model="form[0].value"
            v-on:change="changeChart()"
            outline
            lg10
        ></v-select>
        <v-list
            subheader
            two-line
          >
            <v-subheader>Indicadores</v-subheader>
            <v-list-tile v-for="(indicador, key) in filteredMacroindicador.indicadores"  :key="key" @click="checkIndicador(indicador)">
              <v-list-tile-action>
                <v-checkbox v-model="indicadores[key].value" ></v-checkbox>
              </v-list-tile-action>
              <v-list-tile-content @click="indicadores[key].value = !indicadores[key].value">
                <v-list-tile-title>{{ indicador.nome }} dd</v-list-tile-title>
              </v-list-tile-content>              
            </v-list-tile>
          </v-list>
          </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ECharts from 'vue-echarts'
import 'echarts/lib/chart/pie'
import 'echarts/lib/chart/bar'
import 'echarts/lib/chart/line'
import 'echarts/lib/component/legend'
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
    filteredMacroindicador () {
      return this.getMacroindicadorById(this.$route.params.idMacroindicador)
    }
  },
  data () {
    return {
        pie,
        bar,
        line,
        form,
        indicadores: form[1].lista,
        chart: {}
    }
  },
  methods: {
      changeChart () {
        console.log(this.indicadores)
        switch (this.form[0].value) {
          case "Pizza": this.chart = this.pie;  break;
          case "Barra": this.chart = this.bar;  break;
          case "Linha": this.chart = this.line; break;
          default: this.chart = {}; break;
        }
      },
      checkIndicador (indicador) {
        console.log(this.indicadores.filter(el => { return el.value }).map(el => el.nome))
        this.chart.xAxis.data = this.indicadores.filter(el => { return el.value }).map(el => el.nome)
      }
  }
}

</script>

<style>
.echarts {
    width: 100% !important;
    /* height: auto !important; */
}
</style>
