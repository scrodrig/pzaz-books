<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link
          class="navbar-item"
          to="/"
        >
          <strong>Pzaz Books</strong>
        </router-link>
        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        :class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link
            class="navbar-item"
            to="/fiction"
          >Fiction</router-link>
          <router-link
            class="navbar-item"
            to="/non-fiction"
          >No Fiction
          </router-link>
        </div>

        <div class="navbar-item">
          <div class="buttons">
            <router-link
              class="button is-light"
              to="/login"
            >
              <strong>Login</strong>
            </router-link>
            <router-link
              class="button is-success"
              to="/cart"
            >
              <span class="icon">
                <i class="fas fa-shopping-cart"></i>
              </span>
              <span>Cart</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view />
    </section>

    <section class="footer">
      <p class="has-text-centered">
        <strong>Pzaz Books</strong> by @scrodig
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      showMobileMenu: false,
      cart:{
        items: [],
      }
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
  },
};
</script>

<style lang="scss">
@import '../node_modules/bulma'
</style>
