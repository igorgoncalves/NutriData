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
        <h4>Form</h4>
        <v-select
            :items="form[0].options"
            :label="form[0].label"
            v-model="form[0].value"
            v-on:change="changeChart()"
            outline
        ></v-select>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
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
  data () {
    return {
        pie,
        bar,
        line,
        form,
        chart: {}
    }
  },
  methods: {
      changeChart () {
        switch (this.form[0].value) {
          case "Pizza": this.chart = this.pie;  break;
          case "Barra": this.chart = this.bar;  break;
          case "Linha": this.chart = this.line; break;
          default: this.chart = {}; break;
        }
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
