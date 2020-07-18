<template>
  <div class="container">
    <nuxt-link :to="{ path: 'search' }">
      <b-button>一覧へ</b-button>
    </nuxt-link>
    <p></p>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <nuxt-link :to="{ path: 'search' }">
        <b-button type="submit" variant="primary"
          >この条件で検索</b-button
        ></nuxt-link
      >
      <!-- どうやって　search_fに結果を受け渡せるのだろうか。       -->
      <b-button type="reset" variant="danger">すべてリセット</b-button>
      <b-form-group id="input-group-3" label="都道府県:" label-for="input-3">
        <b-form-checkbox-group
          id="input-3"
          v-model="form.prefecture"
          :options="prefectures"
          name="flavour-1"
        ></b-form-checkbox-group>
      </b-form-group>
      <b-form-group id="input-group-4" label="最小年齢:" label-for="input-4">
        <b-form-select
          id="input-4"
          v-model="form.age_min"
          :options="age_mins"
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-5" label="最大年齢:" label-for="input-5">
        <b-form-select
          id="input-5"
          v-model="form.age_max"
          :options="age_maxs"
        ></b-form-select>
      </b-form-group>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>
<style scoped>
.box {
  display: inline-block;
  width: 100px;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      api_url: "http://localhost:5000",
      form: {
        prefecture: null,
        age_min: 17,
        age_max: 31
      },
      prefectures: [
        // { text: "Select One", value: null },
        "北海道",
        "青森県",
        "岩手県",
        "宮城県",
        "秋田県",
        "山形県",
        "福島県",
        "茨城県",
        "栃木県",
        "群馬県",
        "埼玉県",
        "千葉県",
        "東京都",
        "神奈川県",
        "新潟県",
        "富山県",
        "石川県",
        "福井県",
        "山梨県",
        "長野県",
        "奈良県",
        "和歌山県",
        "鳥取県",
        "島根県",
        "岡山県",
        "広島県",
        "山口県",
        "徳島県",
        "香川県",
        "愛媛県",
        "高知県",
        "福岡県",
        "佐賀県",
        "長崎県",
        "熊本県",
        "大分県",
        "宮崎県",
        "鹿児島県",
        "沖縄県"
      ],
      age_mins: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      age_maxs: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      show: true
    };
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();
      // alert(JSON.stringify(this.form));
      // console.log(this.form);
      console.log(this.form.age_min);
      console.log(this.form.prefecture);
      let res = await axios.get(this.api_url + "/user_by_conditions", {
        params: {
          age_min: this.form.age_min,
          age_max: this.form.age_max,
          prefecture: this.form.prefecture
        }
      });
      console.log(res.data);
      //flaskへ。api/user_by_conditions
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.age_min = 18;
      this.form.age_max = 30;
      this.form.prefecture = null;
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
