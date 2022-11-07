<template>
  <div>
    <div 
      class="size"
      @click="updateSizeStatus"
      :class="{ 'selected' : size.selected }"
    >
      <div>{{ size.name }}</div>
      <div>{{ size.price }}</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'SizeListItem',
    props: {
      size: Object,
    },
    methods: {
      updateSizeStatus() {
        this.$store.dispatch('updateSizeStatus', this.size)
      }
    }
  }
</script>

<style>
.size {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid black;
  border-radius: 20px;
  margin: 20px 0px 0px 0px;
  padding: 10px;
  height: 100px;
}
.selected {
  background-color: #43936C;
  color: white;
}
</style>