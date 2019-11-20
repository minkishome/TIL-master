import Vue from 'vue'
import App from './App.vue'
import router from './router'  // from './router/index.js'
import store from './store' // from './store/index.js

import VueSession from 'vue-session' // 발급받은 Token을 SessionStorage에 저장하는 것을 도와줌

Vue.config.productionTip = false
Vue.use(VueSession); // Vue 에게 VueSession이라는 middleware 등록

new Vue({
  router,  // router/index.js 에서 악수 하고, 본격적으로 일을 시작.
  store, // store/index.js 에서 악수하고 본격적으로 일을 시작. 
  render: h => h(App)
}).$mount('#app')
