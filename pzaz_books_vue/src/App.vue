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
        <div class="navbar-start">
          <div class="navbar-item">
            <form
              method="get"
              action="/search"
            >
              <div class="field has-addons">
                <div class="control">
                  <input
                    class="input"
                    type="text"
                    placeholder="Search"
                    name="query"
                  />
                </div>
                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
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
            <template v-if="$store.state.isAuthenticated">
              <router-link
                class="button is-light"
                to="/my-account"
              >
                <strong>My Account</strong>
              </router-link>
            </template>
            <template v-else>
              <router-link
                class="button is-light"
                to="/log-in"
              >
                <strong>Login</strong>
              </router-link>
            </template>
            <router-link
              class="button is-success"
              to="/cart"
            >
              <span class="icon">
                <i class="fas fa-shopping-cart"></i>
              </span>
              <span>Cart ({{ cartTotalLength }})</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <div
      class="is-loading-bar has-text-centered"
      :class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

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
import axios from 'axios'
export default {
  name: "App",
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      }
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }

  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let item of this.cart.items) {
        totalLength += item.quantity
      }
      return totalLength
    }
  }
};
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
