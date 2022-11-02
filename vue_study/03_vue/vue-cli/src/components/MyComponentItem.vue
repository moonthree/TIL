<template>
  <div class="border-child">
    <h3>나는 MyComponent의 하위 컴포넌트</h3>
    <h4>{{ staticProps }}</h4>
    <h4>{{ dynamicProps }}</h4>
    <button @click="childToParent">클릭!</button>
    <br>
    <input 
      type="text"
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods: {
    childToParent: function () {
      this.$emit('child-to-parent', '나는 자식이 보낸 데이터다.')
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = null
    }
  },
}
</script>

<style>
  .border-child {
    border: solid 5px #41B883;
    border-radius: 20px;
    margin: 10px;
    padding: 10px;
  }
</style>