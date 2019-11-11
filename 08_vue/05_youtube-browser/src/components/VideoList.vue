<template>

        <ul class="col-lg-4 list-group">
            <VideoListItem 
                v-for="video in videos" 
                :key="video.etag"
                :video="video"
                @videoSelect="onVideoSelect"
            > 
                
            </VideoListItem>
        </ul>

  
</template>

<script>
import VideoListItem from './VideoListItem';
export default {
    name: 'VideoList',
    //props 쓰기 
    // props 는 data랑 똑같이 사용할 수 있다. props === 물려받은 data
    props: { // 배열로 써도 되지만, 객체를 매우 권장.
        videos: Array, 
    },
    components: {
        VideoListItem,
    },
    methods: {
        onVideoSelect (video) {
            this.$emit('videoSelect', video)
        }
    },
}
</script>


<style>


</style>