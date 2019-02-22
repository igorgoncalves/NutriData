<template>
<div>
  <h1>Lista de dimesões</h1>
  <v-data-table
    :headers="headers"
    :items="desserts"
    class="elevation-1"
  >
    <template slot="items" slot-scope="props">
      <td>{{ props.item.name }}</td>
      <td class="text-xs-right">{{ props.item.calories }}</td>
      <td class="text-xs-right">{{ props.item.fat }}</td>
      <td class="text-xs-right">{{ props.item.carbs }}</td>
      <td class="text-xs-right">{{ props.item.protein }}</td>
      <td class="text-xs-right">{{ props.item.iron }}</td>
       <td class="justify-center layout px-0">
            <v-icon
              small
              class="mr-2"
              @click="editItem(props.item)"
            >
              edit
            </v-icon>
            <v-icon
              small
              @click="deleteItem(props.item)"
            >
              delete
            </v-icon>
          </td>
    </template>
  </v-data-table>
</div>
</template>

<script>
  export default {
    data () {
      return {
        headers: [
          {
            text: 'Nome',
            align: 'left',
            sortable: false,
            value: 'name'
          },
          { text: 'Descrição', value: 'descricao' },
          { text: 'Ações', sortable: false, align: 'right', }
        ],
        desserts: [
          {
            name: 'Aquisição de Alimentos',
            descricao: 'Aquisição de Alimentos'
          },
          {
            name: 'Saneamento Básico',
            descricao: 'Valores da dimensão Saneamento básico'
          }
        ]
      }
    }
  }
</script>