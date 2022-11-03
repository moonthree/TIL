<template>
  <div>
    <hr>
    <h2>산출세액계산</h2>
    <h2>산출세액 : {{ afterTax }}</h2>
    <p>세액감면 : (-) {{ taxCredit }} 만원</p>
    <hr>
    <h2>결정세액 : {{ result }}</h2>
  </div>
</template>

<script>
export default {
  name: 'TaxRate',
  props:{
    taxBase: Number,
    taxCredit: Number,
  },
  computed: {
    afterTax() {
      if (this.taxBase <= 1200) {
        return Math.round(this.taxBase * 0.06)
      } else {
        return Math.round(this.taxBase * 0.15)
      }
    },
    result() {
      return this.afterTax - this.taxCredit >= 0 ? this.afterTax - this.taxCredit : 0
    }
  }
}
</script>

<style>

</style>