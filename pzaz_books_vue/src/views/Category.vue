<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-12 has-text-centered">{{ category.name }}</h2>
      </div>

      <BookBox
        class="column is-3"
        v-for="book in category.books"
        :key="book.id"
        :book="book"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { toast } from "bulma-toast"
import BookBox from "@/components/BookBox.vue"

export default {
  name: "Category",
  data() {
    return {
      category: {
        books: []
      }
    }
  },
  components: {
    BookBox
  },
  mounted() {
    this.getCategory()
  },
  watch: {
    $route(to, from) {
      if (to.name === "category") {
        this.getCategory()
      }
    }
  },
  methods: {
    async getCategory() {
      this.$store.commit("setIsLoading", true)
      const categorySlug = this.$route.params.category_slug

      await axios.get(`/api/v1/books/${categorySlug}`)
        .then(response => {
          this.category = response.data
        })
        .catch(error => {
          toast({
            message: "Something went wrong",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 5000,
            position: "top-center",
          })
        })
        .finally(() => {
          this.$store.commit("setIsLoading", false)
        })
    }
  }
}
</script>