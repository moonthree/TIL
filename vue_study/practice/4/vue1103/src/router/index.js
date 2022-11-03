import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import IncomeTaxCalc from '@/views/IncomeTaxCalc'
import ViewFourTwo from '@/views/ViewFourTwo'
import YoutubeView from '@/views/YoutubeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/fourOne',
    name: 'fourOne',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/ViewFourOne.vue')
  },
  {
    path: '/incomeTax',
    name: 'incomeTax',
    component: IncomeTaxCalc
  }, 
  {
    path: '/fourTwo',
    name: 'fourTwo',
    component: ViewFourTwo
  },
  {
    path: '/ssafytube',
    name: 'ssafytube',
    component: YoutubeView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
