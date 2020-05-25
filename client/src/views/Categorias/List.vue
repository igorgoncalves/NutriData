<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout wrap>
      <v-flex md12 sm12 lg12>
        <v-card>
          <v-card-title>
            <v-flex md12 sm12 lg10>
              <h2>Lista de macroindicadores</h2>
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
            :items="categorias"
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
                    <v-icon slot="activator" @click="editItem(props.item.id)">
                      mdi-settings
                    </v-icon>
                  </template>
                  <span>Alterar</span>
                </v-tooltip>

                <v-tooltip top>
                  <template>
                    <v-icon slot="activator" @click="deleteItem(props.item)">
                      mdi-delete
                    </v-icon>
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
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState("categorias", ["categorias"]),
  },
  methods: {
    ...mapActions("categorias", ["fetchCategorias", "deleteCategoria"]),
    createNew() {
      this.$router.push({ path: `/categorias/novo` });
    },
    editItem(categoriaId) {
      this.$router.push({ path: `/categorias/${categoriaId}/update` });
    },
    deleteItem(categoria) {
      this.deleteCategoria(categoria.id);
    },
  },
  mounted() {
    this.fetchCategorias();
  },
  data() {
    return {
      search: "",
      headers: [
        { text: "#", sortable: false },
        {
          text: "Nome",
          value: "nome",
        },
        { text: "Descrição", value: "descricao" },
        { text: "Ações", sortable: false },
      ],
    };
  },
};
</script>
