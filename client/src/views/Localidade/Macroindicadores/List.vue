<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout wrap>
      <v-flex md12 sm12 lg12>
        <v-card>
          <v-card-title>
            <v-flex md12 sm12 lg10>
              <h2>Lista de macroindicadores para {{ filteredLocalidade }}</h2>
            </v-flex>
            <v-layout align-end>
              <v-btn class="success" @click="createNew()">+ Adicionar</v-btn>
            </v-layout>
            <v-spacer></v-spacer>
            <v-flex md12 sm12 lg4 offset-lg8>
              <v-text-field
                v-model="search"
                append-icon="mdi-search"
                label="Buscar (Ex.: Aquisição)"
                single-line
                hide-details
              ></v-text-field>
            </v-flex>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="getMacroindicadores"
            :search="search"
            class="elevation-1"
          >
            <template slot="items" slot-scope="props">
              <td />
              <td>{{ props.item.nome }}</td>
              <td class="text-xs-left">{{ props.item.descricao }}</td>
              <td class="justify-center px-0">
                <v-tooltip top>
                  <template>
                    <v-icon slot="activator" @click="createView(props.item)">mdi-chart-bar</v-icon>
                  </template>
                  <span>Analisar dados</span>
                </v-tooltip>
                <!-- <v-tooltip top>
                  <template>
                    <v-icon
                      slot="activator"
                      @click="showIndicaores(props.item.id)"
                    >
                      mdi-subdirectory-arrow-right
                    </v-icon>
                  </template>
                  <span>Gerenciar indicadores</span>
                </v-tooltip>
                <v-tooltip top>
                  <template>
                    <v-icon
                      slot="activator"
                      @click="editItem(props.item)"
                    >
                      mdi-settings
                    </v-icon>
                  </template>
                  <span>Alterar</span>
                </v-tooltip>
                -->
                <v-tooltip top>
                  <template>
                    <v-icon slot="activator" @click="deleteItem(props.item)">mdi-delete</v-icon>
                  </template>
                  <span>Deletar</span>
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
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters("localidades", ["getLocalidadesPorCodigo"]),
    ...mapGetters("macroindicadores", ["getMacroindicadores"]),
    filteredLocalidade() {
      return this.getLocalidadesPorCodigo(this.$route.params.idLocalidade).nome;
    }
  },
  methods: {
    ...mapActions("macroindicadores", [
      "fetchMacroindicadoresByLocalidade",
      "deleteIndicador"
    ]),
    createNew() {
      this.$router.push({ path: `/macroindicadores/novo` });
    },
    createView(macroindicador) {
      this.$router.push({ path: `/localidade/${this.$route.params.idLocalidade}/macroindicador/${macroindicador.id}/admin` });
    },
    deleteItem(macroindicador) {
      this.deleteIndicador(macroindicador.id);
    }
  },
  mounted() {
    this.fetchMacroindicadoresByLocalidade(this.$route.params.idLocalidade);
  },
  data() {
    return {
      search: "",
      headers: [
        { text: "#", sortable: false },
        {
          text: "Nome",
          value: "nome"
        },
        { text: "Descrição", value: "descricao" },
        { text: "Ações", sortable: false }
      ]
    };
  }
};
</script>
