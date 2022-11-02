<template>
  <div id="AppParent">
    <h1>AppParent</h1>
    <input type="text" v-model="dataParent" @input="parent">
    <p>appData: {{downApp}}</p>
    <p>childData: {{ childData }}</p>
    <AppChild
      :data-parent="dataParent"
      :down-app="downApp"
      @up-child="upChild"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild';

export default {
  name: 'AppParent',
  components: {
    AppChild
  },
  props:{
    downApp:String
  },
  data: function() {
    return{
      dataParent: null,
      childData: null
    }
  },
  methods: {
    upChild: function (child) {
      this.$emit('up-child', child)
      this.childData = child
    },
    parent: function() {
      this.$emit('up-parent', this.dataParent)
    }
  }
}
</script>

<style>
#AppParent{
  border: 5px solid orange;
  border-radius: 20px;
  margin: 5px;
}
</style>