<template>
  <div>
    <div class="order">
      <img :src="order.menu.image"/>
      <div>
        <div>{{ order.menu.title }}</div>
        <div>사이즈: {{ order.size.name }}</div>
      </div>
      <div class="order-price">
        <div>가격: {{ totalPrice }}원</div>
        <div>
          {{ order.optionItem[0].type }} {{order.optionItem[0].count}}회 |
          {{ order.optionItem[1].type }} {{order.optionItem[1].count}}회 |
          {{ order.optionItem[2].type }} {{order.optionItem[2].count}}회
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'OrderListItem',
    props: {
      order: Object,
    },
    computed: {
      totalPrice() {
        let optionTotal = 0
        this.order.optionItem.forEach((el) => {
          console.log(el)
          optionTotal += el.price * el.count
        })

        return this.order.menu.price + this.order.size.price + optionTotal
      },
    },
  }
</script>

<style>
.order{
  display: grid;
  grid-template-columns: 5% 73% 22%;
  padding: 20px 0px 20px 0px;
  border-bottom: 1px solid #DBDDE2;
  align-items: center;
}
.order > img {
  width: 50px;
  height: 50px;
  border-radius: 20px;
}
/* .order-price{
  text-align: right;
} */
</style>