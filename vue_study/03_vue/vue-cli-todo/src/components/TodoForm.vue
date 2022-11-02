<template>
  <div id="todo-form">
    <h1>TodoForm</h1>
    <input
      type="text"
      v-model="todoTitle"
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">입력</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null
    }
  },
  methods: {
    createTodo: function () {
      this.$emit('create-todo', this.todoTitle)
      this.todoTitle = null
    }
  }
}
</script>

<style>
  #todo-form{
    margin: 10px;
    border: 5px solid greenyellow;
    padding: 10px;

  }
</style>