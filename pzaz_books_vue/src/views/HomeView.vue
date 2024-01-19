<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <div class="container">
          <h1 class="title mb-6">
            Pzaz Books
          </h1>
          <h2 class="subtitle">
            The best books from the best book store
          </h2>
        </div>
      </div>
    </section>


    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">
          Latest Books
        </h2>
      </div>

      <div
        class="column is-3"
        v-for="book in latestBooks"
        :key="book.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img
              :src="book.get_thumbnail"
              :alt="book.title"
              class="resized-image"
            />
          </figure>
          <h3 class="is-size-4">{{ book.name }}</h3>
          <p class="is-size-6 has-text-grey">{{ book.price }}</p>
          View Details
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"


export default {
  name: "HomeView",
  data() {
    return {
      latestBooks: [],
    };
  },
  components: {
  },
  mounted() {
    this.getLastestBooks()
  },
  methods: {
    getLastestBooks() {
      axios.get("/api/v1/latest-books/")
        .then(response => {
          this.latestBooks = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
.resized-image{
  display: block;
  width: 100%;
  height: 500px;
}
</style>

