<template>
    <form @submit.prevent="onSubmit">
        <input type="text" v-model="content">
        <button type="submit">Add Todo</button>
    </form>
</template>

<script>
export default {
    name: 'AddTodo',
    methods: {
        onSubmit() {
            console.log('submit', this.content);
            if (this.content.trim()) {
                const newTodo = {
                    content: this.content,
                    completed: false,
                }
                this.$emit('add-todo', newTodo);
                this.content = "";
            }
        }
    },
    data() {
        return {
            content: '',
        }
    }
}
</script>

<style scoped>
    form {
        display: flex;
        margin-bottom: 12px;
    }
    input {
        width: 700px;
    }
    button {
        width: 75px;
        margin-left: 25px;
    }
</style>