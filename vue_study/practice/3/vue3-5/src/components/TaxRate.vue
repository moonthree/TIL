<template>
  <div>
    <hr>
    <h2>산출세액 : {{ calTax }}만원</h2>
    <h2>세액감면 : (-) {{ taxRelief }} 만원</h2>

    <FinalTax 
      :taxRelief="taxRelief"
      :calTax="calTax"
    />
  </div>
</template>

<script>
import FinalTax from '@/components/FinalTax';

export default {
  name: 'TaxRate',
  props:{
    taxBase: Number,
    taxRelief: Number,
  },
  components:{
    FinalTax,
  },
  data: function () {
    return {
      calTax: 0
    }
  },
  methods:{
    calc: function () {
      if (this.taxBase <= 1200) {
        this.calTax = Math.round(this.taxBase * 0.06)
      } else if (this.taxBase > 1200 && this.taxBase <= 4600) {
        this.calTax = Math.round(this.taxBase * 0.15)
      } else {
        this.calTax = Math.round(this.taxBase * 0.24)
      }
    }
  },
  watch: {
    taxBase() {
      this.calc()
    }
  }
}
</script>

<style>

</style>