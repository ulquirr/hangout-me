<template>
  <CreateHangout @add-hangout="addHangout" />
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
    };
  },
  async created() {},
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

      console.log(this.hangouts);
    },
  },
};
</script>
