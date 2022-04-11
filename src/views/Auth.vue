<template>
  <div class="container">
    <form @submit="onSubmit" class="add-form">
      <div class="form-control">
        <label>Login</label>
        <input type="text" v-model="login" name="login" placeholder="Type your login" />
        <label>Password</label>
        <input type="password" v-model="password" name="password" placeholder="Type your password" />
      </div>
      <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
      <ul>
        <li class="error" v-for="error in errors" :key="error"> {{ error }}</li>
      </ul>
      </p>
      <input type="submit" value="Sign in" class="btn btn-block" />
    </form>
  </div>
</template>

<script>
import { LOG_IN_USER, CALL_SNACK_BAR } from "../mutation-types";
import router from "../router"

export default {
  name: "Auth",
  data() {
    return {
      login: "",
      password: "",
      errors: [],
      show: false,
      msg: "",
      status: null
    };
  },
  async created() { },
  methods: {
    async onSubmit(e) {
      let error = false
      e.preventDefault();
      if (this.checkForm() === true) {
        const user = { login: this.login, password: this.password }
        await fetch(`http://127.0.0.1:8000/user/create`, {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify(user),
        }).catch((e) => error = true)

        if (!error) {
          this.$store.commit(LOG_IN_USER, { ...user, isLoggedIn: true })
          this.msg = 'You are logged in!'
          this.title = "";
          this.content = "";
          this.status = true

          router.push('/')
        } else {
          this.msg = 'Log in failed, verify your credentials!'
          this.status=false
        }
        this.show = true
      }

      const snackBarOptions = {status: this.status, msg: this.msg, show: this.show}

       this.$store.commit(CALL_SNACK_BAR, snackBarOptions)

       const clearSnackBar = () => {
         this.$store.commit(CALL_SNACK_BAR, {})
       }

      setTimeout(clearSnackBar, 3000)


    },
    checkForm: function (e) {


      this.errors = [];

      if (!this.login) {
        this.errors.push("Name required.");
      } else if (this.login.length < 4) {
        this.errors.push("Name length should be at least 4 symbols.");
      }
      if (!this.password) {
        this.errors.push("password is required.");
      } else if (this.password.length < 4) {
        this.errors.push("Name length should be at least 4 symbols.");
      }

      return this.errors.length == 0
    },
  },
};
</script>


<style scoped>
.error {
  margin-left: 20px;
  color: red
}
</style>