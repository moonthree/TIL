<template>
  <div>
    <div class="option">
      <div>{{ option.type }}</div>
      <div class="option-div">
        <button @click="decrease">-</button>
        <span>{{ option.count }}</span>
        <button @click="increase">+</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'OptionListItem',
    props: {
      option: Object,
    },
    methods: {
      increase() {
        this.$store.dispatch('increase', this.option)
      },
      decrease() {
        this.$store.dispatch('decrease', this.option)
      },
    },
  }
</script>

<style>
.option {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid black;
  border-radius: 20px;
  margin: 20px 0px 0px 0px;
  padding: 10px;
  height: 100px;
}
.option-div > button{
  width: 30px;
  height: 30px;
  border-radius: 50%;
}
.option-div > span{
  margin: 0px 10px 0px 10px;
}
</style>