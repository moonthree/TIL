<template>
  <div>
    <h1>2. 사이즈를 고르세요.</h1>
    <SizeListItemVue
      v-for="size in sizeList"
      :key="size"
      :size="size"
    />
  </div>
</template>

<script>
import SizeListItemVue from './SizeListItem.vue';

export default {
  name: 'SizeList',
  components:{
    SizeListItemVue
  },
  // methods: {
  //   onSelectMenu: function () {},
  // },
  computed: {
    sizeList() {
      return this.$store.state.sizeList
    }
  },
}
</script>

<style>
</style>