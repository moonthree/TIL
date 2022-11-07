import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, message) {
      console.log('mutation-state : ', state)
      console.log('mutation-message : ', message)
      state.message = message
    }
  },
  actions: {
    changeMessage(context, message) {
      console.log('action-context : ', context)
      console.log('action-message : ',message)
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
