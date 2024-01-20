<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Cart</h1>
      </div>

      <div class="column is-12 box">
        <table
          class="table is-fullwidth"
          v-if="cartTotalLength"
        >
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            <CartItem
              v-for="item in cart.items"
              :key="item.book.id"
              :initialItem="item"
              @removeFromCart="removeFromCart"
            />
          </tbody>
        </table>

        <p v-else>You don't have any products in your cart...</p>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Summary</h2>
        <strong> ${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
        <hr>
        <router-link
          class="button is-dark"
          to="cart/checkout"
        >
          Proceed to checkout
        </router-link>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
import router from '@/router'
export default {
  name: 'Cart',
  components: {
    CartItem,
    router
  },
  data() {
    return {
      cart: {
        items: [],
      }
    }
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(i => i.book.id !== item.book.id)
    },
  },
  mounted() {
    document.title = 'Pzaz Books - Cart'
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((total, item) => {
        return total + item.quantity
      }, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((total, item) => {
        return total + (item.quantity * item.book.price)
      }, 0)
    },
  },
}
</script>

<style scoped>
/* Your component's styles go here */
</style>
