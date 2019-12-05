<template>
  <v-app>
    <!-- <core-filter v-if="false" /> -->
    <component :is="layout">
      <core-view />
      <v-dialog v-model="loading" persistent width="350">
        <v-card color="primary" dark>
          <v-card-text>
            Aguarde alguns instantes
            <v-progress-linear indeterminate color="white" class="mb-0" />
          </v-card-text>
        </v-card>
      </v-dialog>
    </component>
  </v-app>
</template>

<script>
import { mapActions, mapMutations } from "vuex";

export default {  
  methods: {
    ...mapMutations("app", ["onLoading", "offLoading"])
  },
  computed: {
    layout(){
      return (this.$route.meta.layout || 'public')  + '-template';
    },
    loading: {
      get: function() {
        return this.$store.state.app.loading;
      },
      set: function(newValue) {}
    }
  }
};
</script>


<style lang="scss">
@import "@/styles/index.scss";

/* Remove in 1.2 */
.v-datatable thead th.column.sortable i {
  vertical-align: unset;
}

</style>
