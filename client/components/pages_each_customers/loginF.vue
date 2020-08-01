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
    <div class="auth_status_msg_container">
      <p class="auth_status_msg">{{ auth_status_message }}</p>
    </div>
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
      proccessing: false,
      auth_status_message: ""
    };
  },
  methods: {
    login: async function() {
      axios
        .post(this.api_url + "api/login", {
          mail: this.mail,
          password: this.password
        })
        .then(response => {
          console.log("Everything is awesome.");
          console.log(response);
        })
        .catch(error => {
          console.warn("Not good man :(");
          this.auth_status_message = error.response.data.message;
        });

      // let res = await axios.post(this.api_url + "api/login", {
      //   // params: {
      //   mail: this.mail,
      //   password: this.password
      //   // }
      // });
      // console.log(res);
    }
  }
};
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
.auth_status_msg_container {
  height: 30px;
}
.auth_status_msg {
  margin: auto;
  text-align: center;
  margin-top: 10px;
  color: #ff0000;
}
</style>
