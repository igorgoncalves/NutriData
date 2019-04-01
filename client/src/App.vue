<template>
  <v-app>
    <!-- <core-filter v-if="false" /> -->

    <core-toolbar v-if="$route.name === 'Home'" />

    <core-drawer v-if="$route.name !== 'Home'" />

    <core-view />
  </v-app>
</template>

<style lang="scss">
@import '@/styles/index.scss';

/* Remove in 1.2 */
.v-datatable thead th.column.sortable i {
  vertical-align: unset;
}
body, #app {
    background: white !important;
  }
</style>
