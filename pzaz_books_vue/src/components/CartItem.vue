<template>
  <tr>
    <td><router-link :to="item.book.get_absolute_url">{{ item.book.name }}</router-link></td>
    <td>${{ item.book.price }}</td>
    <td>
      {{ item.quantity }}
    </td>
    <td>${{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete"></button>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CartItem',
  props: {
    initialItem: Object
  },
  data() {
    return {
      item: this.initialItem
    }
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.book.price
    },
  },
}
</script>