import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
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
        price: 3500,
        selected: false,
        image : "https://source.unsplash.com/featured/?cappuccino"
      },
      {
        title: '마끼아또',
        price: 4000,
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
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '아이스크림',
        price: 1000,
        count: 0,
      },
      {
        type: '크로플',
        price: 7500,
        count: 0,
      },
    ]
  },
  getters: {
  },
  mutations: {
    SHOPPING(state, order) {
      state.orderList.push(order)
      console.log(state.orderList)
      state.optionList.forEach((el) => {
        el.count = 0
      })
      state.sizeList.forEach((el) => {
        el.selected = false
      })
      state.menuList.forEach((el) => {
        el.selected = false
      })
      return state
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
    },
    INCREASE(state, optionItem) {
      state.optionList = state.optionList.map((option) => {
        if (option === optionItem) {
          option.count += 1
        }
        return option
      })
    },
    DECREASE(state, optionItem) {
      state.optionList = state.optionList.map((option) => {
        if (option === optionItem) {
          if( option.count === 0) {
            alert('0개임')
            return
          } else {
            option.count -= 1
          }
        }
        return option
      })
    }
  },
  actions: {
    updateMenuStatus(context, menuItem) {
      context.commit('UPDATE_MENU_STATUS', menuItem)
    },
    updateSizeStatus(context, sizeItem) {
      context.commit('UPDATE_SIZE_STATUS', sizeItem)
    },
    shopping(context, optionItem) {
      let menu = ''
      let size = ''
      this.state.menuList.forEach((el) => {
        if (el.selected) {
          menu = el
        }
      })
      this.state.sizeList.forEach((el) => {
        if (el.selected) {
          size = el
        }
      })
      if (menu === '' && size === '') {
        alert('음료와 사이즈를 선택하세요')
        return
      } else if (menu === '' ) {
        alert('음료를 선택하세요')
        return
      } else if (size === '' ) {
        alert('사이즈를 선택하세요')
        return
      }
      // const option = this.state.optionList
      // console.log(option[0])
      // console.log(optionItem)
      const order = {menu, size, optionItem}
      context.commit('SHOPPING', order)
    },
    increase(context, optionItem) {
      context.commit('INCREASE', optionItem)
    },
    decrease(context, optionItem) {
      context.commit('DECREASE', optionItem)
    }
  },
  modules: {
  }
})