<template>
    <div>
        <!-- <input @input="onInput" type="text"> -->
        <input @keypress.enter="onInput" type="text">
        <!-- method는 내가 인자를 추가로 넘긴다면 () 붙이고 -->
        <!-- 그게 아니라면 () 안 붙임 -->
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput (e) {  // e 를 쓰지 않아도 event 가 변수로 넘어오지만 써줘도 무관
            // console.log(e.target.value)
            // this.$emit('Event이름', 전송할 값) => 자식 cmpnt => 부모 cmpnt 데이터를 올려보낼 때.
            this.$emit('inputChange', e.target.value);
        }
    }
}
</script>


<style scoped> 
/* scoped : 해당 컴포넌트의 태그들만 영향을 받는다. */
    input {
        width:75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }
</style>