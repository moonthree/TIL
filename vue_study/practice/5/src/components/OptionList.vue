<template>
  <div>
    <h1>3. 옵션을 고르세요.</h1>
    <OptionListItemVue
      v-for="(option, idx) in optionList"
      :key="idx"
      :option="option"
    />
  </div>
</template>

<script>
  import OptionListItemVue from './OptionListItem.vue';

  export default {
    name: 'OptionList',
    components: {
      OptionListItemVue,
    },
    computed: {
      optionList() {
        return this.$store.state.optionList
      },
    },
    // methods: {
    //   increase: function () {
    //   },
    //   decrease: function () {
    //   },
    // },
  }
</script>

<style>
</style>