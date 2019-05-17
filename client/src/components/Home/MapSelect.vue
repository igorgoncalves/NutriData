<template>
  <div>
     <v-flex xs12>
    <v-btn
      class="succes"
      dark
      icon
      @click="localidade = '0'"
    >
      Brasil
    </v-btn>
    <v-btn
      class="succes"
      dark
      icon
      @click="localidade = '2'"
    >
      Nordeste
    </v-btn>
    <v-btn
      class="succes"
      dark
      icon
      @click="localidade = '28'"
    >
      Sergipe
    </v-btn>
  </v-flex>
  <transition-group name="fade" tag="div">
    <img svg-inline v-show="showBrasil" key="Brasil" class="icon" src="./brasil.svg" alt="example" />
    <img svg-inline v-show="showNordeste" key="Nordeste" class="icon" src="./nordeste.svg" alt="example" />
    <img svg-inline v-show="showSergipe" key="Sergipe" class="icon" src="./sergipe.svg" alt="example" />
  </transition-group>
  </div>
</template>

<script>
export default {
  props: ['value'],
  data () {
    return {
      localidade: 0,
      colors: ['#81C784', '#66BB6A', '#43A047', '#388E3C', '#2E7D32']
    }
  },
  mounted () {
    document.querySelectorAll('path').forEach(element => {      
      element.addEventListener('click', () => (this.localidade = element.getAttribute('class')))

    })
  },
  computed: {
    showBrasil () {
      return this.localidade < 10 && !this.showNordeste
    },
    showNordeste () {

      return (this.localidade === '2' || this.localidade > 10) && !this.showSergipe
    },
    showSergipe () {
      return this.localidade === '28' || this.localidade > 1000
    }
  },
  watch: {
    localidade: function () {
      this.$emit('input', this.localidade)
    }
  }

}

</script>

<style scoped>
  .succes {
    width: 80px !important;
    margin: 15px;
    background:#16a085 !important;
  }
  path {
    fill: #16a085;

  }
  path:hover, path:active {
    fill: #ff6f00 !important; 
  }

  .fade-enter-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>
