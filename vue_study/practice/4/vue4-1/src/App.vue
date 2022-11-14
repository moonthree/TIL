<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <ReserveTime/>
  </div>
</template>

<script>
import ReserveTime from '@/components/ReserveTime';

export default {
  name: 'App',
  components: {
    ReserveTime
  }
}
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
