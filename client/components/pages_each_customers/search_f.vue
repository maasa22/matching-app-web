<template>
  <div>
    <h1>search for women</h1>
    <div v-for="(user_male, index) in users_male" :key="index">
      <p>{{ user_male.id_user }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      users_male: [],
      api_url: "http://localhost:5000"
    };
  },
  methods: {
    getMaleUsers: async function() {
      let res = await axios.get(this.api_url + "/users_f");
      console.log(res.data);
      this.users_male = res.data;
    }
  },
  created: function() {
    this.getMaleUsers();
  }
};
</script>
