<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="toHome">홈으로!</button>
    <br>
    <br>
    <input 
      type="text"
      @keyup.enter="goToHello"
      v-model="inputData"
      placeholder="엔터치면 이동함"
    >
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData : null
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    goToHello() {
      this.$router.push({ name:'hello', params: { userName: this.inputData }})
    }
  }
}
</script>