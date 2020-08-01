<template>
  <div>
    <search-f
      :age_min="age_min"
      :age_max="age_max"
      :prefectures="prefectures"
    />
  </div>
</template>
<script>
import searchF from "~/components/pages_each_customers/searchF.vue";
// import search_m from "~/components/pages_each_customers/searchM.vue";
export default {
  components: {
    searchF
    // searchM
  },
  data() {
    return {
      age_min: 0,
      age_max: 0,
      prefectures: []
    };
  },
  created() {
    //もしあれば。
    this.age_min = this.$route.query.age_min;
    this.age_max = this.$route.query.age_max;
    this.prefectures = this.$route.query.prefectures;
    // console.log(this.age_min, this.age_max, this.prefectures);
  }
};
</script>
