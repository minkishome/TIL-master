import Vue from 'vue';
import App from './App.vue';


new Vue({
    //el : '#app', === .$mount('#app') 같은 의미, 뒤에 쓴다 $mount는
    //method(함수 in 객체) 정의할 때,  () => 금지이지만 여기서만 쓴다. 
    render:h => h(App),

}).$mount('#app')