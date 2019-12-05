<template functional>
  <v-hover>
    <v-card
      max-width
      :shaped="true"
      slot-scope="{ hover }"
      :class="`elevation-${hover ? 12 : 2}`"
      class="mx-auto d-flex flex-no-wrap"
    >
      <v-flex xs7 md10 sm10 lg10>
        <v-card-text>
          <v-tooltip left>
            <template>
              <p slot="activator" class="title text--primary">{{ props.macroindicador.nome }}</p>
            </template>
            <span>{{ props.macroindicador.descricao }}</span>
          </v-tooltip>
          <div class="text--primary text-truncate">{{ props.macroindicador.descricao }}</div>
        </v-card-text>
      </v-flex>
      <v-flex xs2 md2 sm2 lg2 class="justify-center">
        <v-card-actions>
          <v-btn
            color="success accent-4"
            :to="`/localidade/${props.codigoLocalidade}/macroindicador/${props.macroindicador.id}`"
          >Ver dados</v-btn>
        </v-card-actions>
      </v-flex>
    </v-card>
  </v-hover>
</template>
<script>
import Macroindicador from "../../models/macroindicador";

export default {
  props: {
    macroindicador: {
      type: Macroindicador
    },
    codigoLocalidade: Number
  }
};
</script>

<style>
.v-card__text {
  text-align: initial;
}

.v-card__actions {
  margin: 0 !important;
}
</style>