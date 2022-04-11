import { createStore } from 'vuex'
import { LOG_IN_USER, LOG_OUT_USER, CALL_SNACK_BAR  } from './mutation-types'


// Create a new store instance.
const store = createStore({
  state() {
    return {
      user: {},
      snackBar: {}
    }
  },
  mutations: {
    [LOG_IN_USER] (state, payload) {
      state.user = payload
    },
    [LOG_OUT_USER] (state,) {
      state.user = {}
    },
    [CALL_SNACK_BAR] (state, payload) {
      state.snackBar = payload
    }
  }
})


export default store
