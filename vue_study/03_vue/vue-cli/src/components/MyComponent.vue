<template>
  <div class="border">
    <h1>이거는 내가 만든 새로운 컴포넌트다!!</h1>
    <MyComponentItem 
      static-props="MyComponent에서 props로 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
//1. 불러오기
import MyComponentItem from '@/components/MyComponentItem';

export default {
  name: 'MyComponent',
  // 2. 등록하기
  components: {
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: '이건 동적인 데이터임!',
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log(childData)
    },
    getDynamicData: function (event) {
      console.log(`사용자가 입력한 값은 ${event}입니다.`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 5px black;
    border-radius: 20px;
  }
</style>