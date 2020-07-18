<template>
  <div class="container">
    <h1>さがす</h1>
    <p class="box">12345 人</p>
    <nuxt-link :to="{ path: 'search_by_conditions' }">
      <b-button class="box">検索</b-button>
    </nuxt-link>
    <div class="row">
      <div
        v-for="(user_male, index) in users_male"
        :key="index"
        class="col-md-3 col-6 my-1"
      >
        <nuxt-link :to="{ path: 'user/' + user_male.id_user }">
          <b-card
            :title="user_male.display_name"
            :img-src="user_male.self_images"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2 h-100"
          >
            <b-card-text>
              {{ user_male.age }}歳, {{ user_male.prefecture }}<br />
              {{ user_male.self_status_message }} <br />
              <!-- <hr />
            {{ user_male.self_introduction.slice(0, 50) }} -->
            </b-card-text>
            <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
          </b-card>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      users_male: [],
      users_male_rows: [],
      api_url: "http://localhost:5000"
    };
  },
  methods: {
    getMaleUsers: async function() {
      let res = await axios.get(this.api_url + "/users_m");
      console.log(res.data);
      this.users_male = res.data;
      // 全然違う。
      // for (i = 0; i < int(users_male.length / 3); i++) {
      //   users_row = this.users_male_rows.append([i, i + 1, i + 2]);
      // }
    }
  },
  created: function() {
    this.getMaleUsers();
  }
};
</script>
<style scoped>
.box {
  display: inline-block;
  width: 100px;
}
</style>
