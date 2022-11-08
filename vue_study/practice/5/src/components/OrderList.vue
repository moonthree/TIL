<template>
  <div>
    <div class="order-div">
      <h1>주문 내역</h1>
      <p>총 {{totalOrderCount}}건: {{totalOrderPrice}}원</p>
      <OrderListItemVue
        v-for="(order, idx) in orderList"
        :key="idx"
        :order="order"
      />
    </div>
  </div>
</template>

<script>
  import OrderListItemVue from './OrderListItem.vue';
  export default {
    name: 'OrderList',
    components: {
      OrderListItemVue
    },
    computed: {
      orderList () {
        return this.$store.state.orderList
      },
      totalOrderCount () {
        return this.$store.state.orderList.length
      },
      totalOrderPrice () {
        let price = 0
        this.$store.state.orderList.forEach((el) => {
          price += el.menu.price
          price += el.size.price
        })
        return price
      },
    },
  }
</script>

<style>
.order-div{
  background-color: #F3F4F6;
  border-radius: 20px;
  padding: 40px 20px 20px 20px;
  text-align: left;
}
.order-div > p {
  margin: 20px 0px 20px 0px;
  font-weight: bold;
}
</style>