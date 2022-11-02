<template>
  <div id="app-child">
    <h1>AppChild</h1>
    <input type="text" v-model="dataChild" @input="upChild">
    <p>appData: {{ downApp }}</p>
    <p>parentData: {{ dataParent }}</p>
    <p>childData: {{ dataChild }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  data: function() {
    return{
      dataChild: null
    }
  },
  props: {
    dataParent: String,
    downApp: String
  },
  methods: {
    upChild: function () {
      this.$emit('up-child', this.dataChild)
    }
  }
}
</script>

<style>
#app-child{
  border: 5px solid skyblue;
  border-radius: 20px;
  margin: 5px;
}
</style>