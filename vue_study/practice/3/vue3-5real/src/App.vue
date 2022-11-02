<template>
  <div id="app">
    <h1>APP</h1>
    <input type="text" v-model="dataApp">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <AppParent
      @up-child="upChild"
      @up-parent="upParent"
      :down-app="dataApp"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent';

export default {
  name: 'App',
  components: {
    AppParent
  },
  data: function() {
    return{
      dataApp: null,
      childData: null,
      parentData: null,
    }
  },
  methods: {
    upChild: function (child) {
      this.childData = child
    },
    upParent: function (parent) {
      this.parentData = parent
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border: 5px solid black;
  border-radius: 20px;
}
</style>
