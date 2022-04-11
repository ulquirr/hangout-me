<template>
  <CreateHangout v-if="isLoggedIn" @add-hangout="addHangout" />
  <div v-else>
    you need to be authorized
  </div>
</template>

<script>
import CreateHangout from "../components/CreateHangout";
export default {
  name: "Home",
  components: {
    CreateHangout,
  },
  data() {
    return {
      hangouts: [],
      isLoggedIn: false
    };
  },
  async created() {
    this.isLoggedIn = this.$store.state.user.isLoggedIn
   },
  methods: {
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


    },
  },
};
</script>
