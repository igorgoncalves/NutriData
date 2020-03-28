<template>
  <div>
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex md12 sm12 lg4>
          <v-autocomplete
            :items="getLocalidadeNomes"
            item-text="name"
            label="Busque uma localidade"
            v-model="nome"
          ></v-autocomplete>

          <component :is="layoutLocalidade" v-model="localidade"></component>
          <!-- <map-select  /> -->
        </v-flex>
        <v-flex xs1>
          <v-divider hidden-md-and-down vertical></v-divider>
        </v-flex>
        <v-flex xs12 md12 sm12 lg7>
          <div>
            <h2 class="text-orange step-2 display-1">
              Indicadores:
              <strong class="display-1">{{ nomeLocalidade }}</strong>
            </h2>
            <v-layout row wrap>
              <v-flex
                lg12
                md12
                v-for="indicador in macroindicadores"
                :key="indicador.nome + componentKey + Math.random()"
              >
                <card-indicador :macroindicador="indicador" :codigoLocalidade="parseInt(localidade)" />
              </v-flex>

              <section v-if="Object.keys(macroindicadores).length === 0" style="display: contents;">
                <span style="margin: 0 auto">Nenhum indicador disponivel para esse local</span>
              </section>
              
            </v-layout>
          </div>
        </v-flex>

        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
          <v-card>
            <v-btn class="close" @click="dialog = false">Voltar</v-btn>
            <show-graph :idMacroindicador="idMacroindicador" :idLocalidade="localidade" />
          </v-card>
        </v-dialog>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import MapSelect from "@/components/Home/MapSelect";
import ListSelect from "@/components/Home/ListSelect";
import ViewGraph from "@/components/Macroindicador/CreateView";
import CardIndicador from "../components/Home/CardIndicador";


import Macroindicador from "../models/macroindicador";

import { mapGetters, mapActions, mapMutations } from "vuex";

export default {
  components: {
    "map-select": MapSelect,
    "list-select": ListSelect,
    "show-graph": ViewGraph,
    "card-indicador": CardIndicador
  },
  data() {
    return {
      localidade: 0,
      componentKey: 0,
      showChart: true,
      nome: "",
      dialog: false,
      idMacroindicador: null
    };
  },
  computed: {
    ...mapGetters("macroindicadores", ["getMacroindicadores"]),
    ...mapGetters("localidades", [
      "getLocalidadeName",
      "getLocalidadeNomes",
      "getCodigoLocalidadePorNome"
    ]),
    layoutLocalidade() {
      return this.$mq !== "lg" || this.$mq !== "xl" ? "list-select" : "map-select";
    },
    macroindicadores() {
      return this.getMacroindicadores;
    },
    nomeLocalidade() {
      return this.getLocalidadeName(this.localidade);
    }
  },
  watch: {
    nome: function(nomeSelecionado) {
      this.localidade = this.getCodigoLocalidadePorNome(nomeSelecionado);
    },
    localidade: function() {
      this.onLoading();
      this.fetchMacroindicadoresByLocalidade(this.localidade);
    }
  },
  methods: {
    ...mapActions("macroindicadores", [
      "fetchMacroindicadoresByLocalidade",
      "fetchMacroindicadoresByIdandLocaliade"
    ]),
    ...mapActions("localidades", ["fetchLocalidades"]),
    ...mapMutations("app", ["onLoading", "offLoading"]),
    ...mapMutations("chart", ["load"]),
    showVisao(idMacroindicador) {
      this.idMacroindicador = idMacroindicador;
      this.fetchMacroindicadoresByIdandLocaliade({
        codigoLocalidade: this.localidade,
        idMacroindicador
      });
      this.$router.push({
        path: `/localidade/${this.localidade}/macroindicador/${idMacroindicador}`
      });

      // this.dialog = true;
    }
  },
  mounted() {
    this.fetchMacroindicadoresByLocalidade(this.localidade);
    this.fetchLocalidades();
    this.onLoading();
    this.$store.subscribe((mutation, state) => {
      switch (mutation.type) {
        case "macroindicadores/updateMacroindicadores":
        case "macroindicadores/updateMacroindicador":
          this.offLoading();
          break;
      }
    });
  }
};
</script>

<style scoped>
.fade-enter-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.text-orange {
  color: #ffa21a;
}
</style>
