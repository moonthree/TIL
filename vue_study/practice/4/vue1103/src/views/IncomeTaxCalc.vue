<template>
  <div>
    <h1>소득세 계산기</h1>
    <div>
      <label for="incone">연봉 입력 (만원) : </label>
      <input type="number" id="income" v-model.number="income">
    </div>

    <div>
      <label for="tax-credit">세액감면액 (만원) : </label>
      <input type="number" id="tax-credit" v-model.number="taxCredit">
    </div>

    <TotalIncome
      :income="income"
      :tax-credit="taxCredit"
    />
  </div>
</template>

<script>
import TotalIncome from '@/components/income/TotalIncome'

export default {
  name: 'IncomeTaxCalc',
  data: function () {
    return {
      income: 0,
      taxCredit: 0,
    }
  },
  components:{
    TotalIncome,
  }
}
</script>

<style>

</style>