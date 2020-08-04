<template>
    <li>
      <span  @click="$emit('complete-todo', todo.id)" class="pointer" :class="{done: todo.is_completed}">
        <strong>{{ index + 1 }}</strong>
        {{todo.content}}
      </span>
      <button class="pointer" @click="$emit('delete-todo', todo.id)">&times;</button>
    </li>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    todo: Object,
    index: Number,
  },
}
</script>

<style scoped>
  li {
    border: 1px solid black;
    display: flex;
    justify-content: space-between;
    padding: .5rem 2rem;
    margin-bottom: 1rem;
  }

  button {
    background-color:red;
    color: white;
    border: 2px solid white;
    border-radius: 50%; 
  }

  input {
    margin-right: 1 rem;
  }

  .done {
    text-decoration: line-through;
  }

  .pointer {
    cursor: pointer;
  }
</style>
