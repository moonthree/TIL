import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '../views/HelloView.vue'
import LoginView from '../views/LoginView.vue'
import NotFound404 from '../views/NotFound404.vue'
import DogView from '../views/DogView.vue'
Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn) {
        console.log('이미 로그인 되어있음')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 전역 가드
// router.beforeEach((to, from, next) => {
//   // 로그인 여부
//   const isLoggedIn = false

//   // 로그인이 필요한 페이지
//   const authPage = ['hello']
//   const isAuthRequired = authPage.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     console.log('로그인으로 이동')
//     next({name: 'login'})
//   } else {
//     console.log('to로 이동')
//     next()
//   }
// })

export default router
