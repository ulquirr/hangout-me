<template>
  <SearchFlight @add-flight="addFlight" :api_key="this.api_key" />
</template>

<script>
import SearchFlight from "../components/SearchFlight";
export default {
  name: "Home",
  components: {
    SearchFlight,
  },
  data() {
    return {
      fligts: [],
      api_key: process.env.VUE_APP_API_KEY,
    };
  },
  async created() {},
  methods: {
    async addFlight(iata_code) {
      const res = await fetch(
        `http://api.aviationstack.com/v1/flights?access_key=${this.api_key}&flight_iata=${iata_code}&limit=1`,
        {
          method: "GET",
        }
      );

      const data = await res.json();

      this.fligts = [
        ...this.fligts,
        data.data[Math.floor(Math.random() * data.data.length)],
      ];

      console.log(this.fligt);
    },
  },
};
</script>
