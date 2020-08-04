<template>
  <div>
    <ul>
        <TodoItem 
            :key="todo.id" 
            v-for="(todo, idx) in todos" 
            :todo="todo" 
            :index="idx"
            @delete-todo="deleteTodo"
            @complete-todo="completeTodo"
        />
    </ul>
  </div>
</template>

<script>
import TodoItem from '@/components/TodoItem';

export default {
  name: 'TodoList',
  components: {
      TodoItem
  },
  props: {
    todos: Array
  },
  methods: {
      deleteTodo(id) {
        this.$emit('delete-todo', id);
      },
      completeTodo(id) {
        this.$emit('complete-todo', id);
      }
  }
}
</script>

<style scoped>
  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
</style>
