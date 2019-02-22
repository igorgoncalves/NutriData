<template>
    <div>
        <tree
            :data="treeData"
            :options="treeOptions"
            @node:selected="onNodeSelected"
        />
    </div>
</template>

<script>
import LiquorTree from 'liquor-tree'

export default {
  name: 'tree-fields',
  components: {
    [LiquorTree.name]: LiquorTree
  },
  data: () => ({
    treeData: [
      { text: '2. Hortaliças' },
      { text: '2.1. Hortaliças folhosas e florais' },
      { text: '2.3. Hortaliças tuberosas e outras' },
      { text: '3. Frutas' },
      { text: '3.1. Frutas de clima tropical' },
      { text: '3.2. Frutas de clima temperado' }

    ],
    treeOptions: {
      dnd: true
    }
  })
}
</script>

<style scoped>

</style>
