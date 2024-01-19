<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img
            :src="book.get_image"
            :alt="book.title"
            class="resized-image"
          />
        </figure>
        <h1 class="title">{{ book.name }}</h1>
        <p>
          {{ book.description }}
        </p>

      </div>
      <div class="column is-3">
        <h2 class="subtitle">Information:</h2>
        <p>
          <strong>Price:</strong>
          $ {{ book.price }}
        </p>
        <div class="field has-addons mt-6">
          <div class="control">
            <input
              type="number"
              class="input"
              min="1"
              :model="quantity"
            />
          </div>
          <div class="control">
            <a class="button is-dark">Add to cart</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "Book",
  data() {
    return {
      book: {},
      quantity: 1
    };
  },
  mounted() {
    this.getBook()
  },
  methods: {
    getBook() {

      const category_slug = this.$route.params.category_slug
      const book_slug = this.$route.params.book_slug

      axios.get(`/api/v1/books/${category_slug}/${book_slug}`)
        .then(response => {
          this.book = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>

<style scoped>
.resized-image {
  display: block;
  width: 100%;
  height: 100%;
}
</style>