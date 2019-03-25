<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex
        md12
        sm12
        lg12>
        <v-card>
          <v-card-title>
            <v-flex
              md12
              sm12
              lg10
            >
              <h2>Lista de localidades</h2>
            </v-flex>
            <v-layout
              align-end
            >
            </v-layout>
            <v-spacer></v-spacer>
            <v-flex
              md12
              sm12
              lg4
              offset-lg8
            >
              <v-text-field
                v-model="search"
                append-icon="mdi-search"
                label="Buscar (Ex.: Aracaju)"
                single-line
                hide-details
              ></v-text-field>
            </v-flex>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="getLocalidades"
            :search="search"
            class="elevation-1"
          >
            <template
              slot="items"
              slot-scope="props">
              <td />
              <td>{{ props.item.codigo }}</td>
              <td class="text-xs-left">{{ props.item.nome }}</td>
              <td class="justify-center px-0">
                <v-tooltip top>
                  <template>
                    <v-icon
                      slot="activator"
                      @click="showMacroindicadores(props.item.codigo)"
                    >
                      mdi-subdirectory-arrow-right
                    </v-icon>
                  </template>
                  <span>Gerenciar indicadores</span>
                </v-tooltip>
              </td>
            </template>
          </v-data-table>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('localidades', ['getLocalidades'])
  },
  methods: {
    ...mapActions('localidades', ['fetchLocalidades']),
    showMacroindicadores (codigoLocalidade) {
      this.$router.push({ name: 'Macroindicadores', params: { codigo: codigoLocalidade }})

    }
  },
  mounted () {
    this.fetchLocalidades()
  },
  data () {
    return {
      search: '',
      headers: [
        { text: '#', sortable: false },
        { text: 'Código', value: 'codigo' },
        { text: 'Nome', value: 'nome' },
        { text: 'Ações', sortable: false }
      ],
      desserts: this.getLocalidades
    }
  }
}
</script>
