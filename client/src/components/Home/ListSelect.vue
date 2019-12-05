<template>
  <div>
    <v-flex xs12>
      <v-btn  md4 :class="{ active: localidade == 0 }" class="btn-localidade fixo" dark icon @click="localidade = 0">Brasil</v-btn>
      <v-btn :class="{ active: localidade == 2 }" class="btn-localidade fixo" dark icon @click="localidade = 2">Nordeste</v-btn>
      <v-btn :class="{ active: localidade == 28 }" class="btn-localidade fixo" dark icon @click="localidade = 28">Sergipe</v-btn>
    </v-flex>
    <v-flex d-flex xs12 style="flex-wrap: wrap">      
        <v-flex  justify="center" v-for="local in localidadesExibidas" :key="local.codigo">
          <v-btn :class="{ active: localidade == local.codigo }" class="btn-localidade" dark icon @click="localidade = local.codigo">{{local.nome}}</v-btn>
        </v-flex>
      
    </v-flex>
  </div>
</template>

<script>
import { mapGetters, mapState } from "vuex";

export default {
  props: ["value"],
  data() {
    return {
      localidade: 0,
      colors: ["#81C784", "#66BB6A", "#43A047", "#388E3C", "#2E7D32"],
      nomeLocalidade: "",
      filter: l => l.codigo < 10 && l.codigo != 0
    };
  },
  mounted() {},
  methods: {},
  computed: {
    ...mapState("localidades", ["localidades"]),
    ...mapGetters("localidades", ["getLocalidadeName"]),
    localidadesExibidas() {
      return this.localidades.filter(this.filter);
    },
    showBrasil() {
      return this.localidade < 10 && !this.showNordeste;
    },
    showNordeste() {
      return (
        (this.localidade === 2 || this.localidade > 10) && !this.showSergipe
      );
    },
    showSergipe() {
      return this.localidade === 28 || this.localidade > 1000;
    }
  },
  watch: {
    localidade: function() {
      this.$emit("input", this.localidade);      
      if (this.showBrasil) {
        this.filter = l => l.codigo < 10 && l.codigo != 0;
      } else if (this.showNordeste) {
        this.filter = l => l.codigo > 10 && l.codigo < 100;
      } else if (this.showSergipe) {
        this.filter = l => l.codigo > 10000;
      }
    }
  }
};
</script>

<style scoped>

.btn-localidade {
  width: 100% !important;
  padding: 15px !important;
  background: #16a085 !important;
}

.btn-localidade.active {  
  background: #ff6f00 !important;
}

.btn-localidade.fixo {
  width: 80px !important;
  margin: 15px;
}

path {
  fill: #16a085;
}
path:hover,
path:active {
  fill: #ff6f00 !important;
}

.fade-enter-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.tooltip {
  position: fixed;
  z-index: 100;

  padding: 10px 20px;

  border: 1px solid #b3c9ce;
  border-radius: 4px;
  text-align: center;
  font: italic 14px/1.3 sans-serif;
  color: #333;
  background: #fff;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.3);
}

/* .tooltip {
      display:block;
      position:fixed;
      overflow:hidden;
  } */
</style>

