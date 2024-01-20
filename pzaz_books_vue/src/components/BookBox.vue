<template>
  <div class="column is-3">
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

      <router-link
        :to="book.get_absolute_url"
        class="button is-dark mt-4"
      >
        View Details
      </router-link>

    </div>
  </div>
</template>

<script>
export default {
  name: "BookBox",
  props: {
    book: Object
  }
}
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}

.resized-image {
  display: block;
  width: 100%;
  height: 500px;
}
</style>