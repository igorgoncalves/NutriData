<template>
    <v-app>
       <!-- <v-navigation-drawer
        class="blue lighten-3"
        permanent
        fixed
        left
        app
      >
        <v-list>
          <v-list-tile
            v-for="item in menus"
            :key="item.title">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer> -->
      <v-toolbar app></v-toolbar>
      <v-content>
        <v-container fluid>
          <router-view></router-view>
        </v-container>
      </v-content>
      <!-- <v-footer app></v-footer> -->
    </v-app>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      menus: [
        {title: 'Home', icon: ''},
        {title: 'About', icon: ''},
        {title: 'Visoes', icon: ''},
        {title: 'Macroindicador', icon: ''},
        {title: 'Login', icon: ''}
      ]
    }
  }
}
</script>

<style>
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
