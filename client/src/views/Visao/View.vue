<template>
  <div>
    <create-view ref="createview" :idMacroindicador="idMacroindicador" />
  </div>
</template>

<script>

import CreateView from '@/components/Macroindicador/CreateView'
import { mapActions, mapMutations } from 'vuex'

export default {
  components: {    
    'create-view': CreateView
  },
  data () {
    return {
    }
  },
  computed :{  
    idMacroindicador () {
      return this.$route.params.idMacroindicador;     
    }
  },  
}

</script>

<style>
</style>