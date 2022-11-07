<template>
  <div class="menu-list">
    <h1>1. 음료를 고르세요.</h1>
    <div>
      <MenuListItemVue
        v-for="(menu, index) in menuList"
        :key="index"
        :menu="menu"
      />
    </div>
  </div>
</template>

<script>
import MenuListItemVue from './MenuListItem.vue';

export default {
  name: 'MenuList',
  components: {
    MenuListItemVue
  },
  computed: {
    menuList() {
      return this.$store.state.menuList
    },
  },
  // methods: {
  //   selectMenu: function () {},
  // },
}
</script>

<style>

</style>