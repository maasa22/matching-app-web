<template>
  <div class="login">
    <div v-if="proccessing" class="text-center">Please wait...</div>

    <b-form-input
      v-model="mail"
      type="text"
      class="input-form"
      placeholder="Mail"
    ></b-form-input>

    <b-form-input
      v-model="password"
      class="input-form"
      type="password"
      placeholder="Password"
    ></b-form-input>

    <b-button v-on:click="login" variant="primary" class="btn-block"
      >Log me in</b-button
    >
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      mail: "",
      password: "",
      api_url: process.env.BASE_URL,
      proccessing: false
    };
  },
  methods: {
    login: async function() {
      let res = await axios.post(this.api_url + "api/login", {
        // params: {
        mail: this.mail,
        password: this.password
        // }
      });
      console.log(res);
    }
  }
};

// let res = await axios.post(this.api_url + "user_by_conditions", {
//   headers: {
//     "Content-Type": "application/json;charset=utf-8",
//     "Access-Control-Allow-Origin": "*"
//   },
//   params: {
//     age_min: 17,
//     age_max: 31,
//     prefectures: ""
//   }
// });
// console.log(res);
// let res = await axios.post("api/login", {
// headers: {
//   "Content-Type": "application/json;charset=utf-8",
//   "Access-Control-Allow-Origin": "*",
//   "Access-Control-Allow-Methods":
//     "GET, POST, PUT, POST, DELETE, OPTIONS"
// },
</script>

<style scoped>
.login {
  width: 500px;
  border: 1px solid #cccccc;
  background-color: #ffffff;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
}
.input-form {
  margin-bottom: 9px;
}
</style>
