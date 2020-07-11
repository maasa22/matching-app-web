<template>
  <div class="container">
    <div>
      <!-- <Logo /> -->
      <h1 class="title">
        matching-app-web
      </h1>
      <p>v-for="(book, index) in books" :key="index">{{ book }}</p>
      <button @click="getBooks">get books</button>
      <p>{{ books_tmp }}</p>
      <!-- <div class="links">
        <a
          href="https://nuxtjs.org/"
          target="_blank"
          rel="noopener noreferrer"
          class="button--green"
        >
          Documentation
        </a>
        <a
          href="https://github.com/nuxt/nuxt.js"
          target="_blank"
          rel="noopener noreferrer"
          class="button--grey"
        >
          GitHub
        </a>
      </div> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      books: ["hello", "hi"],
      books_tmp: "",
      api_url: "http://localhost:5000"
    };
  },
  methods: {
    getBooks: async function() {
      let res = await axios.get(this.api_url + "/books");
      console.log(res.data);
      this.books_tmp = res.data;
    }
  }
};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

/* .links {
  padding-top: 15px;
} */
</style>
