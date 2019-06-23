<template>
  <v-content>
    <div id="core-view">
      <div v-if="alert.message" :class="`alert ${alert.type}`">{{alert.message}}</div>
      <v-fade-transition mode="out-in">        
        <router-view />
      </v-fade-transition>
    </div>    
  </v-content>
</template>

<script>
export default {
  metaInfo () {
    return {
      title: 'NutriData'
    }
  },
  computed: {
    alert () {
      return this.$store.state.alert
    }
  },
  watch:{
    $route (to, from){
      // clear alert on location change
      this.$store.dispatch('alert/clear');
    }
  } 
}
</script>

<style>
#core-view {
  padding-bottom: 100px;
}
</style>
