 <template>
  <div class="register">
    <b-form-input v-model="mail" type="text" class="input-form" placeholder="Mail"></b-form-input>

    <b-form-input v-model="password" class="input-form" type="password" placeholder="Password"></b-form-input>

    <b-button v-on:click="register" variant="primary" class="btn-block">Register</b-button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      mail: "",
      password: "",
      api_url: process.env.BASE_URL
    };
  },
  methods: {
    register: async function() {
      console.log(this.api_url);
      let res = await axios.post(this.api_url + "register", {
        params: {
          mail: this.mail,
          password: this.password
        }
      });
      console.log(res);
    }
  }
};
</script>

<style scoped>
.register {
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
