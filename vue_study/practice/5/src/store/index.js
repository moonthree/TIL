import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false,
        image : "https://source.unsplash.com/featured/?americano"
      },
      {
        title: '카푸치노',
        price: 3000,
        selected: false,
        image : "https://source.unsplash.com/featured/?cappuccino"
      },
      {
        title: '마끼아또',
        price: 3000,
        selected: false,
        image : "https://source.unsplash.com/featured/?macchiato"
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: false,
      },
      {
        name: 'medium',
        price: 1000,
        selected: false,
      },
      {
        name: 'large',
        price: 1500,
        selected: false,
      },
    ],
  },
  getters: {
  },
  mutations: {
    ADD_ORDER() {

    },
    UPDATE_MENU_LIST() {

    },
    UPDATE_SIZE_LIST() {

    },
    UPDATE_MENU_STATUS(state, menuItem) {
      state.menuList = state.menuList.map((menu) => {
        if (menu === menuItem) {
          menu.selected = !menu.selected
        } else {
          menu.selected = false
        }
        return menu
      })
    },
    UPDATE_SIZE_STATUS(state, sizeItem) {
      state.sizeList = state.sizeList.map((size) => {
        if (size === sizeItem) {
          size.selected = !size.selected
        } else {
          size.selected = false
        }
        return size
      })
    }
  },
  actions: {
    updateMenuStatus(context, menuItem) {
      context.commit('UPDATE_MENU_STATUS', menuItem)
    },
    updateSizeStatus(context, sizeItem) {
      context.commit('UPDATE_SIZE_STATUS', sizeItem)
    }
    
  },
  modules: {
  }
})