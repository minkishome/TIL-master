//auth.js 인증관련 모든 state를 작성
// state에 접근/변경 하는 모든 로직은 여기로
const state = {
    token: null,
};

//Vuex 에서는 Arrow function을 사용한다. 
//getters는 state를 가져오기 위해 첫 인자로 state를 넘어온다.
const getters = {
    isLoggedIn:state => !!state.token, // 특정 값을 true/false로 바꾸는 구문

    
};

const mutations = {
    setToken: (state, token) =>state.token = token,
};

const actions = {
    // logOut: (options) => {
        // mutations.setToken(state, null) === 굉장히 안 좋은 표현식
        // options.commit('setToken', null) // GOOD!
    logout : ({commit}) => {
        commit('setToken', null) // GOOD 코드와 같은 표현
    },
    // login: ({commit}) => {
        
    // },
    login: ({ commit }, token)   => {
        commit('setToken', token)
    }
};

export default {
    state, getters, mutations, actions
}