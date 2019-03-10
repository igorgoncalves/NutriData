<template>
  <div>
    <img svg-inline v-show="showBrasil" class="icon" src="@/assets/brasil.svg" alt="example" />
    <img svg-inline v-show="showNordeste" class="icon" src="@/assets/nordeste.svg" alt="example" />
    <img svg-inline v-show="showSergipe" class="icon" src="@/assets/sergipe.svg" alt="example" />
  </div>
</template>

<script>
export default {
  props: ['value'],
  data () {
    return {
      localidade: 0
    }
  },
  mounted () {
    document.querySelectorAll('path').forEach(element =>
      element.addEventListener('click', () => (this.localidade = element.getAttribute('class'))))
  },
  computed: {
    showBrasil () {
      return this.localidade < 10 && !this.showNordeste
    },
    showNordeste () {
      console.log(this.localidade)
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
  /* svg {
    width: 60%;
    height: 60%;
  } */
  path:hover {
    fill: brown;
  }
</style>
