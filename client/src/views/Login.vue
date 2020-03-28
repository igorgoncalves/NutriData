<template>
    <div>
    <v-content>
      <v-container fluid fill-height>
       <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login</v-toolbar-title>                
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field v-on:keyup.enter="handleSubmit" v-model="username"  name="login" label="Login" type="text"></v-text-field>
                  <v-text-field v-on:keyup.enter="handleSubmit" v-model="password" id="password"  name="password" label="Password" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="#ffa21a" @click="handleSubmit" style="margin: 0 20px 10px 20px">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
        </v-container>
    </v-content>
    </div>
</template>

<script>
export default {
    data () {
        return {
            username: '',
            password: '',
            submitted: false
        }
    },
    computed: {
        loggingIn () {
            return this.$store.state.authentication.status.loggingIn;
        }
    },
    created () {        
        this.$store.dispatch('authentication/logout');
    },
    methods: {
        handleSubmit (e) {
            this.submitted = true;
            const { username, password } = this;
            const { dispatch } = this.$store;
            if (username && password) {
                dispatch('authentication/login', { username, password });
            }
        }
    }
};
</script>

<style scoped>
.v-toolbar .v-toolbar__content .v-toolbar__title {
    color:white;
}
</style>
