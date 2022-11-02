<template>
  <div>
    <p>
      연봉 입력 (만원): 
      <input type="number" v-model="salary" @input="salaryChange">
    </p>
    <p>
      세액감면액 (만원):
      <input type="number" v-model="taxRelief">
    </p>
    <hr>
    <h2>종합소득금액 : {{ salary }} 만원</h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과제표준 : {{ taxBase }}</h2>
    <TaxRate 
      :taxBase="taxBase"
      :taxRelief="taxRelief"
    />
  </div>
</template>

<script>
import TaxRate from '@/components/TaxRate';

export default {
  name: 'InCome',
  components: {
    TaxRate,
  },
  data: function () { 
    return {
      salary: 0,
      taxRelief: 0,
      taxBase: 0,
    }
  },
  methods: {
    salaryChange: function () {
      if (this.salary - 150 >= 0 ) {
        this.taxBase = this.salary-150
      }
    }
  }
}
</script>
