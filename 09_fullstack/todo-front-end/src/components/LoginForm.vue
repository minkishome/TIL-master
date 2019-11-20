<template>
  <div class="login-form">
      <div v-if="isLoading" class="spinner-border" role="status">
        <span class="sr-only">Loading</span>
      </div>


    <form v-else class="login-input" @submit.prevent="login">
        <div v-if="errors.length" class="error-list alert alert-danger">
            <h4> 아래의 오류를 해결해 주세요</h4>
            <ul>
                <li v-for="(error, idx) in errors" :key="idx">
                    {{ error }}
                </li>
            </ul>
        </div>
        <div class="form-group">
            <label for="id">ID</label>
            <input 
                    v-model="credentials.username"
                    type="text" 
                    class="form-control" 
                    id="id" 
                    placeholder="아이디를 입력해주세요"
                    >
        </div>

        <div class="form-group">
            <label for="password">Password</label>
            <input 
                    v-model="credentials.password"
                    type="password" 
                    class="form-control" 
                    id="password" 
                    placeholder="비밀번호를 입력해주세요"
            >
            <button class="btn btn-primary">로그인</button> 
        </div>
        
    </form>
    
    
  </div>
</template>

<script>
// import { METHODS } from 'http'
import router from '../router'
const axios = require('axios')
export default {
    name: 'LoginForm',
    data() {
        return {

            credentials: {
                username:null,
            }, // 1.  id, password에 해당하는 data
            isAuthenticated: false, // 인증 여부
            isLoading: false,
            errors: [],
        }
    },
    methods:{
        login() {
            this.isLoading = true;
            if (this.checkUserInput()) {    
                console.log("django 서버로 데이터를 보냅니다.");
                axios.post('http://localhost:8000/api-token-auth/', this.credentials)
                .then(res => {
                    this.isloading = false;
                    this.$session.start();
                    this.$session.set('jwt', res.data.token)
                    // dispatch => action을 실행하는 methods
                    this.$store.dispatch('login',res.data.token)

                    router.push('/');
                })
                .catch(err => {
                    if(!err.response) {
                        this.errors.push('Network error......')
                    }
                    
                    else if (err.response.status === 400) {
                        this.errors.push('Invaild username or password');
                    } 
                    else if (err.response.status === 500 ) {
                        this.errors.push('Internal Server error. Please try again');
                    }
                    else {
                        this.errors.push('Some error occured')
                    }
                    this.isLoading = false;
                });
                
            
        }
        else {
            this.isLoadgin = false;
        }
        },
        checkUserInput() {
            this.errors= [];
            if (!this.credentials.username) this.errors.push("username 을 입력하세요");
            if (this.credentials.password.length < 8) this.errors.push("password 는 8자 이상입니다.");
            if (!this.errors.length) return true;

        
        },

    }
}
</script>

<style>

</style>