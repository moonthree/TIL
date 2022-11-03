<template>
  <div class="container">
    <div>
      <h1>
        유튜브임
      </h1>
      <section v-if="isSelectedVideo">
        <div>
          <div>
          {{ selectedVideo.snippet.title }}
          </div>
          <div class="ratio ratio-16x9">
            <iframe :src="videoSrc" frameborder="0"></iframe>
          </div>
          <br>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = ''

export default {
  name:'YoutubeView',
  created() {
    axios.get(API_URL, {
      params: {
        key: API_KEY,
        type: 'video',
        part: 'snippet',
        q: '코딩노래',
      }
    }).then((response) => {
      console.log(response.data)
      this.videos = response.data.items
      this.selectedVideo = this.videos[0]
    }).catch((error) => {
      console.log(error)
    })
  },
  data() {
    return {
      videos: [],
      selectedVideo: {}
    }
  },
  computed: {
    videoSrc() {
      const url = 'http://www.youtube.com/embed/'
      return url + this.selectedVideo.id.videoId
    },
    isSelectedVideo() {
      //길이가 1 이상이면 true
      return !!Object.keys(this.selectedVideo).length 
    }
  }
}
</script>

<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>