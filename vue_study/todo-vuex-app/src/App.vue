<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>All Todos: {{ allTodosCount }}</h2>
    <h2>Completed Todos : {{ completedTodosCount }}</h2>
    <h2>Uncompleted Todos : {{ unCompletedTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
    <br>
    <br>
    <!-- <button @click="loadTodos">Todo 불러오기</button> -->
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue';
import TodoForm from './components/TodoForm.vue';

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  methods: {
    // loadTodos() {
    //   this.$store.dispatch('loadTodos')
    // }
  },
  computed: {
    allTodosCount() {
      return this.$store.getters.allTodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    unCompletedTodosCount() {
      return this.$store.getters.unCompletedTodosCount
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
