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
      <div class="select-box">
        <OptionListVue/>
      </div>
    </div>
    <div 
      class="btn"
      @click="shopping"
    >
      장바구니 담기
    </div>
    <OrderListVue/>
  </div>
</template>

<script>
import MenuListVue from './components/MenuList.vue';
import SizeListVue from './components/SizeList.vue';
import OrderListVue from './components/OrderList.vue';
import OptionListVue from './components/OptionList.vue';

export default {
  name: 'App',
  components: {
    MenuListVue,
    SizeListVue,
    OrderListVue,
    OptionListVue
  },
  methods: {
    shopping() {
      this.$store.dispatch('shopping')
    }
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
  width: 400px;
  text-align: left;
}
.btn {
  background-color: white;
  border: 3px solid #43936C;
  margin: 20px 0px 20px 0px;
  border-radius: 20px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 20px;
  color: #43936C;
}
.btn:hover{
  background-color: #43936C;
  color: white
}
</style>
