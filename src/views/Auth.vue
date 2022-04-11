<template>
  <div class="container">
    <form @submit="onSubmit" class="add-form">
      <div class="form-control">
        <label>Login</label>
        <input
          type="text"
          v-model="login"
          name="login"
          placeholder="Type your login"
        />
        <label>Password</label>
        <textarea
          rows="5"
          cols="55"
          type="password"
          v-model="password"
          name="password"
          placeholder="Type your password"
        />
      </div>
        <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
            <li class="error" v-for="error in errors" :key={error}>{{ error }}</li>
       </ul>
        </p>
      <input type="submit" value="Sign in" class="btn btn-block" />
    </form>
  </div>
</template>

<script>
export default {
  name: "Auth",
  data() {
    return {
      login: "",
      password: "",
      errors: [],
    };
  },
  async created() {},
  methods: {
    async onSubmit(e) {
        e.preventDefault();
        this.checkForm()
    },
    async addHangout(hangout) {
      console.log(hangout);
      await fetch(`http://127.0.0.1:8000/hangout/create`, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(hangout),
      });

      this.hangouts = [...this.hangouts, hangout];

      console.log(this.hangouts);
    },
    checkForm: function (e) {
      if (this.name && this.age) {
        return true;
      }

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