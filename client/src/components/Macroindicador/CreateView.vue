<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout wrap>
      <v-flex offset-lg1 md8 sm8 lg7>
        <h2
          style="margin: 0;line-height:1em !important"
        >{{ macroindicador.nome }} [{{ nomeLocalidade }}]</h2>
        <small>{{ macroindicador.fonte }}</small>

        <v-chart v-if="chart" :options="chart" ref="chart" autoresize />
        <v-flex md12 sm12 lg12>
          <span>{{ macroindicador.descricao }}</span>
        </v-flex>
      </v-flex>

      <v-flex md12 sm12 lg4 scroll>
        <v-select
          :items="form[0].options"
          :label="form[0].label"
          v-model="form[0].value"
          v-on:change="changeChart()"
          outline
        ></v-select>
        <v-card>
          <v-list subheader>
            <v-subheader>Anos</v-subheader>
            <v-list-tile v-for="(ano, key) in anos" :key="key+'ano'">
              <v-list-tile-action>
                <v-checkbox v-model="anos[key].value" @change="updateChart"></v-checkbox>
              </v-list-tile-action>
              <v-list-tile-content @click="anos[key].value = !anos[key]">
                <v-list-tile-title>{{ ano.label }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
        <v-card>
          <v-list subheader two-line class="lista-indicadores">
            <v-subheader>Indicadores</v-subheader>
            <v-list-tile v-for="(indicador, key) in indicadores" :key="key">
              <v-list-tile-action>
                <v-checkbox v-model="indicadores[key].value" @change="updateChart"></v-checkbox>
              </v-list-tile-action>
              <v-list-tile-content @click="indicadores[key].value = !indicadores[key]">
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
import { mapGetters, mapActions, mapState } from "vuex";
import ECharts from "vue-echarts";
import "echarts/lib/chart/pie";
import "echarts/lib/chart/bar";
import "echarts/lib/chart/line";
import "echarts/lib/component/legend";
import "echarts/lib/component/legend/ScrollableLegendModel.js";
import "echarts/lib/component/legend/ScrollableLegendView.js";
import "echarts/lib/component/legend/scrollableLegendAction.js";
import "echarts/lib/component/toolbox";
import "echarts/lib/component/toolbox/feature/SaveAsImage";

import pie from "./ChartsDefault/pie";
import bar from "./ChartsDefault/bar";
import line from "./ChartsDefault/line";
import form from "./ChartsDefault/form";

export default {
  props: ["idMacroindicador", "idLocalidade"],
  components: {
    "v-chart": ECharts
  },
  computed: {
    ...mapState("macroindicadores", ["macroindicador"]),
    anosSelecionados() {
      return this.anos ? this.anos.filter(el => {
        return el.value && el.value != false;
      }) : [];
    },
    indicadoresSelecionados() {
      return this.indicadores.filter(el => {
        return el.value && el.value != false;
      });
    },
    nomeLocalidade() {
      let name = this.getLocalidadeName();
      return name(this.idLocalidade);
    }
  },
  watch: {
    macroindicador() {
      this.anos = undefined;
      this.indicadores = this.macroindicador.indicadores;
      this.indicadores.forEach(indicadores => (indicadores.value = true));
      this.form[0].value = "Pizza";
      this.changeChart();
      this.$refs.chart.clear();
      this.$refs.chart.mergeOptions({});
    },
    indicadores() {
      // if (this.indicadores === undefined) return;
      this.anos = this.anos
        ? this.anos
        : this.indicadores[0].amostras
            .filter(am => am.codigoLocalidade == this.idLocalidade)
            .map(am => {
              return { label: am.ano, value: true };
            });
        this.updateChart()
    }
  },

  data() {
    return {
      indicadores: [],
      pie: pie,
      bar: bar,
      line: line,
      form,
      chart: {},
      type: "",
      anos: undefined
    };
  },
  methods: {
    ...mapActions("macroindicadores", ["fetchMacroindicadoresById"]),
    ...mapActions("visao", ["createVisao"]),
    ...mapGetters("localidades", ["getLocalidadeName"]),
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
      this.updateChart();
    },
    checkIndicador(valor) {
      this.updateChart();
      return valor;
    },
    updateChart() {
      let indicadores = this.indicadoresSelecionados.filter((indicador) => indicador.value);
      let anos = this.anosSelecionados.map(a => a.label);
      var retorno = [];

      switch (this.type) {
        case "pie":
          retorno = indicadores.map(indicador => {
            const valores = indicador.amostras
              .filter(
                am =>
                  am.codigoLocalidade == this.idLocalidade &&
                  anos &&
                  anos.includes(am.ano)
              )
              .map(el => el.valor);
            return {
              name: indicador.nome,
              value: valores ? valores[0] : {}
            };
          });
          this.chart.series[0].data = retorno;
          this.chart.series[0].name = this.macroindicador.unidade;
          this.chart.legend.data = indicadores.map(el => el.nome);
          break;
        case "line":
        case "bar":
          retorno = indicadores.map(indicador => {
            return {
              type: this.type,
              name: indicador.nome,
              data: indicador.amostras
                .filter(
                  am =>
                    am.codigoLocalidade == this.idLocalidade &&
                    anos &&
                    anos.includes(am.ano)
                )
                .map(am => am.valor)
            };
          });
          this.chart.xAxis = {
            type: "category",
            boundaryGap: true,
            axisTick: { show: false },
            data: anos
          };
          this.chart.series = retorno;
          break;
      }
      this.$refs.chart.clear();
      this.$refs.chart.mergeOptions(this.chart);
    },
    send(idMacroindicador) {
      var visao = {};
      visao.tipo_do_grafico = this.type;
      visao.idMacroindicador = idMacroindicador;
      visao.indicadores = this.indicadores.filter(el => {
        return el.value && el.value != false;
      });
      this.createVisao(visao, idMacroindicador);
    }
  },

  mounted() {
    // this.fetchMacroindicadoresById(this.idMacroindicador);
    // this.updateChart()
  }
};
</script>

<style>
.echarts {
  width: 100% !important;
}

.scroll {
  overflow-y: scroll;
  max-height: 100%;
}
</style>
