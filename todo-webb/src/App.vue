<template>
  <div id="app">
    <h1>Todo application</h1>
    <AddTodo @add-todo="addTodo" />
    <TodoList 
      :todos="todos" 
      @delete-todo="deleteTodo"
      @complete-todo="completeTodo"
       />
  </div>
</template>

<script>
import TodoList from '@/components/TodoList';
import AddTodo from '@/components/AddTodo';
const axios = require('axios');

export default {
  name: 'App',
  components: {
    TodoList, AddTodo,
  },
  data() {
    return {
      todos: null,
    }
  },
  mounted() {
    console.log(process.env);
    axios
      .get(`${process.env.VUE_APP_API_URL}api/tasks/`)
      .then(response => (this.todos = response.data));
  },
  methods: {
    deleteTodo(id) {
      axios
        .delete(`${process.env.VUE_APP_API_URL}api/tasks/${id}/`)
        .then(() => {
          this.todos = this.todos.filter(t => t.id !== id);
        })
        .catch(err => console.log(err));
    },
    completeTodo(id) {
      const todo = this.todos.find(t => t.id === id);
      axios
        .patch(`${process.env.VUE_APP_API_URL}api/tasks/${id}/`, {is_completed: !todo.is_completed})
        .then(response => console.log(response))
        .catch(err => console.log(err))
      todo.is_completed = !todo.is_completed
    },
    addTodo(todo) {
      axios
        .post(
          `${process.env.VUE_APP_API_URL}api/tasks/`,
          todo,
          {
            headers: {
              'Content-Type': 'application/json',
            },
          },
        )
        .then(response => {
          this.todos.push(response.data);
        })
        .catch(err => console.log(err))
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
  width: 800px;
  margin: auto;
}
</style>
