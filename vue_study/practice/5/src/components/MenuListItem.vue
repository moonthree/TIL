<template>
  <div>
    <div 
      class="menu"
      @click="updateMenuStatus"
      :class="{ 'selected' : menu.selected }"
    >
      <img :src="menu.image" alt="">
      <div>{{ menu.title }}</div>
      <div>{{ menu.price }}</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MenuListItem',
    props: {
      menu: Object,
    },
    methods: {
      updateMenuStatus() {
        this.$store.dispatch('updateMenuStatus', this.menu)
      }
    }
  }
</script>

<style>
.menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid black;
  border-radius: 20px;
  margin: 20px 0px 0px 0px;
  padding: 10px;
  height: 100px;
}
.menu > img {
  width: 5rem;
  height: 5rem;
  border-radius: 20px;
}
.selected {
  background-color: #43936C;
  color: white;
}

</style>