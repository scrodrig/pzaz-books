import App from "./App.vue";
import axios from "axios";
import { createApp } from "vue";
import router from "./router";
import store from "./store";

axios.defaults.baseURL = "http://localhost:8000";

createApp(App).use(store).use(router, axios).mount("#app");
