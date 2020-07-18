<template>
  <div class="container">
    <div>
      <b-img
        :src="userProfile.self_images"
        fluid
        alt="Responsive image"
      ></b-img>
      <p>{{ userProfile.favorites }} いいね</p>
      <h5>つぶやき</h5>
      <p>{{ userProfile.self_status_message }}</p>
      <h5>自己紹介</h5>
      <p>{{ userProfile.self_introduction }}</p>
      <h5>プロフィール</h5>
      <div class="row">
        <div class="col-md-3 col-3 text-right">所在地</div>
        <div class="col-md-9 col-9 text-left">
          {{ userProfile.prefecture }}
        </div>
        <div class="col-md-3 col-3 text-right">YYY</div>
        <div class="col-md-9 col-9 text-left">
          XXX
        </div>
        <div class="col-md-3 col-3 text-right">YYY</div>
        <div class="col-md-9 col-9 text-left">
          XXX
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      user_id: "",
      userProfile: {},
      api_url: "http://localhost:5000"
    };
  },
  methods: {
    getUserId: function() {
      this.user_id = this.$route.path;
      let res = this.$route.path.split("user/"); //ex. /user/71beb69945ae4
      this.user_id = res[1];
    },
    getUserProfile: async function() {
      let res = await axios.get(this.api_url + "/user/" + this.user_id);
      this.userProfile = res.data[0];
    }
  },
  created: function() {
    this.getUserId();
    this.getUserProfile();
  }
};
</script>
