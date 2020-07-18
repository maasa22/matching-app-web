<template>
  <div class="container">
    <h1>さがす</h1>
    <p class="box">{{ num_of_users }} 人</p>
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
// import searchByConditionsF from "~/components/pages_each_customers/searchByConditionsF.vue";

export default {
  // components: {
  //   searchByConditionsF
  // },
  props: {
    age_min: Number,
    age_max: Number,
    prefectures: Array
  },
  data() {
    return {
      users_male: [],
      users_male_rows: [],
      api_url: "http://localhost:5000",
      num_of_users: 0
      // age_min: this.age_min,
      // age_max: this.age_max,
      // prefectures: this.prefectures
    };
  },
  methods: {
    getMaleUsers: async function() {
      // let res = await axios.get(this.api_url + "/users_m");
      // console.log(this.age_min, this.age_max, this.prefectures);
      if (this.age_min === undefined) {
        this.age_min = 17;
      }
      if (this.age_max === undefined) {
        this.age_max = 31;
      }
      // prefecturesはnullで良いや。flaskのif文でnullの処理する。

      let res = await axios.get(this.api_url + "/user_by_conditions", {
        params: {
          age_min: this.age_min,
          age_max: this.age_max,
          prefectures: this.prefectures
        }
      });
      this.users_male = res.data;
      this.num_of_users = this.users_male.length;
      console.log(this.age_min, this.age_max, this.prefectures);
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
<style>
.box {
  display: inline-block;
  width: 100px;
}
</style>
