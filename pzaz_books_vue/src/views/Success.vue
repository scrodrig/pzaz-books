<template>
  <div class="page-sucess">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>
      </div>

      <div class="column is-12">
        <p>Your order has been placed successfully!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Success',
  data() {
    return {};
  },
  mounted() {
    document.title = 'Success | Pzaz Books';
  },
};
</script>