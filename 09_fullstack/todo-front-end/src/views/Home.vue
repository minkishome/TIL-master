<template>
  <div class="home">
    <h1>This is Home</h1>
    <TodoList />
  </div>  
</template>

<script>

import router from '../router';
import TodoList from '../components/TodoList';

export default {
  name: 'home',
  components: {
    TodoList,
  },
  methods : {
    isLoggedIn() {
      this.$session.start();
      if (this.$session.has('jwt')){ // jwt가 없으면 => login 안됐으면 
        router.push('/login');

      }
    }
    
  },
  create() {
      this.isLoggedIn()
    }
}
</script>
