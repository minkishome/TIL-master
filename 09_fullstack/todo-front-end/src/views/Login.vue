<template>
  <div>
      <h1>로그인 페이지 입니다.</h1>
      <LoginForm /> 
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue'
export default {
    name: 'Login',
    components: {
      LoginForm, 
    },
    // methods : {
    //   isLoggedIn() {
    //     this.$session.start();
    //     if (this.$session.has('jwt')){ // jwt가 없으면 => login 안됐으면 
    //       router.push('/login');

    //     }
    //   }
      
    // },
    // create() {
    //     this.isLoggedIn()
    //   }

}
</script>

<style>

</style>