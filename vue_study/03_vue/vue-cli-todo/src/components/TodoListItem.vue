<template>
  <li class="todo-item">
    {{ todo.title }}
    <button @click="deleteTodo">X</button>
  </li>
</template>

<script>
export default {
  name: 'TodoList',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function () {
      this.$emit('delete-todo', this.todo)
    }
  }
}
</script>

<style>
  .todo-item{
    margin: 10px;
    border: 5px solid orange;
    border-radius: 20px;
  }
</style>