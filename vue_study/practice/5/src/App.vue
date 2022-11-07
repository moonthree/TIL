<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div class="order-app">
      <div class="select-box">
        <MenuListVue/>
      </div>
      <div class="select-box">
        <SizeListVue/>
      </div>
    </div>
  </div>
</template>

<script>
import MenuListVue from './components/MenuList.vue';
import SizeListVue from './components/SizeList.vue';

export default {
  name: 'App',
  components: {
    MenuListVue,
    SizeListVue
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}
ul {
  list-style: none;
}
#app {
  width: 1200px;
  margin: auto;
  text-align: center;
}
.order-app {
  background-color: #DCDCDC;
  display: flex;
  justify-content: center;
  border-radius: 20px;
}
.select-box {
  background-color: white;
  margin: 20px;
  padding: 20px;
  border-radius: 20px;
  width: 600px;
  text-align: left;
}
</style>
