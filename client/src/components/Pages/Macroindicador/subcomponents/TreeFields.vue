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

  mounted() {
    this.$store.subscribe((mutation, state) => {
      const tree = this.$refs.someTree.tree
      switch(mutation.type) {
        case 'updateIndicadores':
          // O componente liquour-tree não atualiza visualmente
          let model = tree.parse(this.treeData)
          this.$set(this.$refs.someTree, 'model', model)
          tree.setModel(model)
          break;
      }
    })
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
