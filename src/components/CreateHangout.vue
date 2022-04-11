<template>
  <div class="container">
    <h1 class="form-title">Create a hangout</h1>
    <form @submit="onSubmit" class="add-form">
      <div class="form-control">
        <label>Hangout title</label>
        <input
          type="text"
          v-model="title"
          name="title"
          placeholder="Type a label for your hangouts"
        />
        <label>Hangout content</label>
        <textarea
          rows="5"
          cols="55"
          type="text"
          v-model="content"
          name="content"
          placeholder="Type something..."
        />
        <label for="date">Hangout date</label>
        <input
          type="date"
          id="date"
          name="date"
          v-model="date"
          :min="date"
          max="2030-12-31"
        />
      </div>
      <input type="submit" value="Save Hangout" class="btn btn-block" />
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateHangout",
  data() {
    return {
      title: "",
      content: "",
      date: new Date().toISOString().split("T")[0],
    };
  },
  methods: {
    async onSubmit(e) {
      e.preventDefault();

      this.$emit("add-hangout", {
        title: this.title,
        content: this.content,
        date: this.date,
      });

      this.title = "";
      this.content = "";
    },
  },
};
</script>

<style >
.container {
  max-width: 500px;
  margin: 150px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.form-title {
  text-align: center;
}
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

.form-control textarea {
  max-width: 100%;
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
