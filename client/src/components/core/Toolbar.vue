<template>
  <v-toolbar id="core-toolbar" flat prominent style="background: #fff;">
    <div class="v-toolbar-title">
      <v-toolbar-title class="tertiary--text font-weight-light">
        <router-link to="/">
          <v-img :src="logo" />
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </div>
    <v-spacer />
    <div class="v-toolbar-items">
      <v-toolbar-items>
        <v-btn color="#ffa21a" @click="goToAdmin()">Admin</v-btn>
      </v-toolbar-items>
    </div>
  </v-toolbar>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  data: () => ({
    notifications: [
      "Mike, John responded to your email",
      "You have 5 new tasks",
      "You're now a friend with Andrew",
      "Another Notification",
      "Another One"
    ],
    title: null,
    responsive: false,
    responsiveInput: false,
    logo: "/static/img/logo.png"
  }),

  watch: {
    $route(val) {
      this.title = val.name;
    }
  },

  mounted() {
    this.onResponsiveInverted();
    window.addEventListener("resize", this.onResponsiveInverted);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResponsiveInverted);
  },

  methods: {
    ...mapMutations("app", ["setDrawer", "toggleDrawer"]),
    onClickBtn() {
      this.setDrawer(!this.$store.state.app.drawer);
    },
    onClick() {
      //
    },
    goToAdmin() {
      this.$router.push({ path: `/macroindicadores` });
    },
    onResponsiveInverted() {
      if (window.innerWidth < 991) {
        this.responsive = true;
        this.responsiveInput = false;
      } else {
        this.responsive = false;
        this.responsiveInput = true;
      }
    }
  }
};
</script>

<style>
#core-toolbar a {
  text-decoration: none;
}
.v-toolbar__content {
  margin-left: 50px !important;
}
.v-toolbar__title {
  margin-left: -30px !important;
  width: 128px;
}
</style>
