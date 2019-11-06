<template>
<!-- 반드시 template 안에는 단 1개 의 태그(노드)가 있어야한다. div 안에!! -->
    <div>
        <h1>{{ filteredInput }}</h1>
        <input type="text" v-model="input">
    </div>
</template>

<script>
export default {
    name: 'App',
    // 왜인지는 모르겠지만 이제부터는 data를 function으로 만들어야함
    data: function() {
       return{ input:'Type SomeThing'}
    },
    methods: {
        
    },
    computed: {
        filteredInput: function() {
            let filter = this.input.replace(/바보|ㅄ|멍청이/g, "**")
            return `Filtered : ${filter}`
            }
        }
    }


</script>

<style></style>