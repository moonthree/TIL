<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <!-- <p>작성시간 : {{ article?.createdAt }}</p> -->
    <p>작성시간 : {{ articleCreatedAt }}</p>
    
    <!-- 삭제 -->
    <button @click="deleteArticle">삭제</button>
    <br>

    <!-- 뒤로가기 -->
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null
    }
  },
  methods: {
    // 게시글 가져오기
    getArticleById(id) {
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      // 반복문을 다 돌았는데 게시글이 없으면
      if (!this.article) {
        this.$router.push({ name: 'NotFound404' })
      }
    },
    // 삭제
    deleteArticle() {
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({ name: 'index' })
    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    }
  }
}
</script>

<style>

</style>