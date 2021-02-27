import Vue from "vue";
import App from "./App";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import axios from "axios";
import Vueaxios from "vue-axios";
//css
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

//vuex
import store from './store'


// Loading
import Loading from 'vue-loading-overlay' //component
import 'vue-loading-overlay/dist/vue-loading.css' //style
Vue.component('Loading', Loading)


//axios
Vue.use(axios, Vueaxios);

//BoostrapVue
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.config.productionTip = false


new Vue({
  el: "#app",
  router,
  store,
  render: h=>h(App),}).$mount('#app')
  // components: { App },
  // template: "<App/>"
// });




