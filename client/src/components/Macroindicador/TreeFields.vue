<template>
  <div>
    <tree
      ref="someTree"
      :data="getIndicadores"
      v-bind:options="treeOptions"
    />
  </div>
</template>

<script>

import LiquorTree from 'liquor-tree'
import { mapGetters, mapActions } from 'vuex'
import Vue from 'vue';

let self = this

export default {
  name: 'TreeFields',
  props: ['idMacroindicador'],
  components: {
    [LiquorTree.name]: LiquorTree
  },
  data: () => ({
    treeOptions: {
      dnd: true,

    }
  }),
  computed: {
     ...mapGetters('indicadores', ['getIndicadores']),
  },
  watch: {
    idMacroindicador () {
      this.getIndicadoresById({ idMacroindicador: this.idMacroindicador })

      const tree = this.$refs.someTree.tree
      let model = tree.parse(this.treeData)
      this.$set(this.$refs.someTree, 'model', model)
      tree.setModel(model)
    }
  },
  methods: {
    ...mapActions('indicadores', ['getIndicadoresById']),
    onNodeSelected (node) {
      console.log(node.text, node)
    }
  },
  mounted () {
    this.$store.subscribe((mutation, state) => {
      console.log("né que foi?")
      switch(mutation.type) {
        case 'indicadores/updateIndicadores':
          const tree = this.$refs.someTree.tree
          let model = tree.parse(this.getIndicadores)
          this.$set(this.$refs.someTree, 'model', model)
          tree.setModel(model)
          break;
      }
    })
  }

}

</script>

<style scoped>

</style>
