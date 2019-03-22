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
              <h2>Lista de macroindicadores</h2>
            </v-flex>
            <v-layout
              align-end
            >
              <v-btn
                primary
                dark
                to="/macroindicador/novo"
              >+ Adicionar</v-btn>
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
                label="Buscar (Ex.: Aquisição)"
                single-line
                hide-details
              ></v-text-field>
            </v-flex>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="desserts"
            :search="search"
            class="elevation-1"
          >
            <template
              slot="items"
              slot-scope="props">
              <td />
              <td>{{ props.item.name }}</td>
              <td class="text-xs-left">{{ props.item.description }}</td>
              <td class="justify-center px-0">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      slot="activator"
                      @click="showIndicaores(props.item)"
                      v-on="on"
                    >
                      mdi-view-module
                    </v-icon>
                  </template>
                  <span>Gerenciar Visões</span>
                </v-tooltip>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      slot="activator"
                      @click="showIndicaores(props.item)"
                    >
                      mdi-subdirectory-arrow-right
                    </v-icon>
                  </template>
                  <span>Gerenciar indicadores</span>
                </v-tooltip>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      slot="activator"
                      @click="editItem(props.item)"
                    >
                      mdi-settings
                    </v-icon>
                  </template>
                  <span>Alterar</span>
                </v-tooltip>
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      slot="activator"
                      @click="editItem(props.item)"
                    >
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
export default {
  data () {
    return {
      search: '',
      headers: [
        { text: '#', sortable: false },
        {
          text: 'Nome',
          value: 'name'
        },
        { text: 'Descrição', value: 'description' },
        { text: 'Ações', sortable: false }
      ],
      desserts: [
        {
          name: 'Aquisição de Alimentos',
          description: 'Aquisição de Alimentos'
        },
        {
          name: 'Saneamento Básico',
          description: 'Valores da dimensão Saneamento básico'
        }
      ]
    }
  }
}
</script>
