<template>
    <div>
        <tree ref="someTree" :data="treeData" :options="treeOptions">
        </tree>
    </div>
</template>

<script>

import LiquorTree from 'liquor-tree'

export default {
  name: 'tree-fields',
  props: ['idMacroindicador'],
  components: {
    [LiquorTree.name]: LiquorTree
  },
  data: () => ({
    treeOptions: {
      dnd: true,
      store: {
        store: this.$store,
        key: 'indicadores',
        mutations: ['initIndicadores', 'updateIndicadores']
      }
    }
  }),
  computed: {
    treeData () {
      return this.$store.getters.getIndicadores
    }
  },
  watch: {
    idMacroindicador () {
      this.$store.dispatch('getIndicadoresById', { idMacroindicador: this.idMacroindicador })

      const tree = this.$refs.someTree.tree
      let model = tree.parse(this.treeData)
      this.$set(this.$refs.someTree, 'model', model)
      tree.setModel(model)
    }
  },
  methods: {
    onNodeSelected (node) {
      console.log(node.text, node)
    }
  }
}

</script>

<style scoped>

</style>
