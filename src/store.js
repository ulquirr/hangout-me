import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
  state () {
    return {
      user: {}
    }
  },
  mutations: {
    updateUser (state, payload) {
      state.user = payload
    }
  }
})


export default store
