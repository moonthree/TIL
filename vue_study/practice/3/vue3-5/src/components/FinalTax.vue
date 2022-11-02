<template>
  <div>
    <hr>
    <h2>결정세액 : {{ result }}만원</h2>
  </div>
</template>

<script>
export default {
  name:'FinalTax',
  props:{
    taxRelief: Number,
    calTax: Number,
  },
  data: function () {
    return {
      result: 0
    }
  },
  methods:{
    calResult: function () {
      if (this.taxRelief < this.calTax) {
        this.result = this.calTax - this.taxRelief
      }
    }
  },
  watch: {
    calTax() {
      this.calResult()
    },
    taxRelief() {
      this.calResult()
    }
  }

}
</script>

<style>

</style>