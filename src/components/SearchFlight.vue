<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <label>Airline name</label>
      <input
        type="text"
        v-model="airline_name"
        name="airline_name"
        placeholder="(American Airlines)"
      />
    </div>

    <input type="submit" value="Save Flight" class="btn btn-block" />
  </form>
</template>

<script>
export default {
  name: "SearchFlight",
  props: {
    api_key: String,
  },
  data() {
    return {
      airline_name: "",
    };
  },
  methods: {
    async getIataCode(airline) {
      const searchQuery = `http://api.aviationstack.com/v1/airlines?access_key=${this.$props.api_key}`;
      const res = await fetch(searchQuery, {
        method: "GET",
      });

      const data = await res.json();

      const airlines = data.data;

      const result = airlines.filter((obj) => obj.airline_name === airline);

      return result[0].iata_code;
    },
    async onSubmit(e) {
      e.preventDefault();

      const iata_code = await this.getIataCode(this.airline_name);

      this.$emit("add-flight", iata_code);

      this.airline_name = "";
    },
  },
};
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}

.form-control {
  margin: 20px 0;
}

.form-control label {
  display: block;
}

.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-control-check label {
  flex: 1;
}

.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
