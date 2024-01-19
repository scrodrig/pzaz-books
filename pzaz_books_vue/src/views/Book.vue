<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-5 is-flex is-justify-content-center">
        <figure class="image mb-6">
          <img
            :src="book.get_image"
            :alt="book.title"
            class="resized-image"
          />
        </figure>
      </div>
      <div class="column is-4">
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
            <a
              class="button is-dark"
              @click="addToCart"
            >Add to cart</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { toast } from "bulma-toast"
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
    async getBook() {
      this.$store.commit("setIsLoading", true)
      const category_slug = this.$route.params.category_slug
      const book_slug = this.$route.params.book_slug

      await axios.get(`/api/v1/books/${category_slug}/${book_slug}`)
        .then(response => {
          this.book = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit("setIsLoading", false)
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity <= 0) {
        this.quantity = 1
      }
      const item = {
        book: this.book,
        quantity: this.quantity
      }
      this.$store.commit("addToCart", item)

      toast({
        message: `Added ${this.book.name} to cart`,
        type: "is-success",
        position: "bottom-right",
        duration: 2000,
        dismissible: true,
        pauseOnHover: true,
      })
    }
  }
};
</script>

<style scoped>
.resized-image {
  /* display: block; */
  width: 100%;
  height: 100%;
}
</style>