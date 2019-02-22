<template>
  <div>
    <p>Home page</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      indicadores: []
    }
  },
  methods: {
    getIndicadores () {
      const path = `http://localhost:5000/api/indicadores`
      axios.get(path)
        .then(response => {
          this.indicadores = response.data.indicadores
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}

</script>
