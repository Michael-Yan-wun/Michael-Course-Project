<template>
  <div>
    <header class="header">
      <a class="header__logo" href="#">Michael小教室</a>
      <div
        class="ham-menu"
        @click="changeVisibility()"
        :class="{ active: burgerVisibility }"
      >
      </div>
      <nav class="header__nav-wrap" :class="{ open: burgerVisibility }">
        <ul class="header__nav-list" @click="burgerVisibility = false">
          <li class="header__nav-item">
            <router-link class="header__nav-link" :to="{name:'COURSE000'}">探索課程</router-link>
          </li>
          <li class="header__nav-item">
            <router-link class="header__nav-link" :to="{name:'login'}">學員登入</router-link>
          </li>
          <li class="header__nav-item">
            <a class="header__nav-link" href="#">Michael</a>
          </li>
        </ul>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      burgerVisibility: false
    }
  },
  methods: {
    changeVisibility() {
      this.burgerVisibility = !this.burgerVisibility;
    }
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.header {
  margin-bottom: 0px;
  display: flex;
  width: 100%;
  background-color: #fff;
  align-items: center;
  position: relative;
  box-sizing: border-box;
  box-shadow: 0px 8px 5px #ccc;
}
@media screen and (min-width: 960px) {
  .header {
    height: 70px;
  }
}
.header__logo {
  display: inline-block;
  height: auto;
  text-decoration: none;
  color: #000;
}

/* Name css 960px為電腦版*/
@media screen and (min-width: 960px) {
  .header__logo {
    margin-left: 24px;
    font-size: 26px;
    letter-spacing: 0.05em;
  }
}
.header__nav-wrap {
  height: 100%;
  width: max-content;
  margin-left: auto;
}
@media screen and (max-width: 959px) {
  .header__nav-wrap {
    position: fixed;
    left: 0;
    top: 0;
    display: none;
    z-index: 10;
    background-color: rgba(0, 0, 0, 0.9);
    width: 100%;
    height: 100%;
  }
}
@media screen and (min-width: 960px) {
  .header__nav-wrap {
    display: inline-block;
    margin-right: 16px;
  }
}
.header__nav-wrap.open {
  display: block;
}
.header__nav-list {
  list-style: none;
  height: 100%;
  margin: 0;
  padding: 0;
}
@media screen and (max-width: 959px) {
  .header__nav-list {
    height: 100%;
    position: relative;
    overflow-x: hidden;
    overflow-y: auto;
    padding-top: 30vh;
  }
}
@media screen and (min-width: 960px) {
  .header__nav-list {
    display: flex;
    align-items: center;
  }
}
.header__nav-item {
  width: max-content;
}
@media screen and (min-width: 1200px) {
  .header__nav-item {
    margin-right: 40px;
  }
}
.header__nav-link {
  position: relative;
  display: inline-block;
  text-decoration: none;
  letter-spacing: 0.15em;
  color: #1a1c1a;
}
@media screen and (min-width: 1200px) {
  .header__nav-link {
    font-size: 18px;
  }
}
.header__nav-link::after {
  position: absolute;
  bottom: -4px;
  left: 0;
  content: "";
  width: 100%;
  height: 2px;
  transform: scale(0, 1);
  transform-origin: center top;
  transition-duration: 0.25s;
}
@media screen and (max-width: 959px) {
  .header__nav-link::after {
    background-color: #fff;
  }
}
@media screen and (min-width: 960px) {
  .header__nav-link::after {
    background-color: #1a1c1a;
  }
}
.header__nav-link:hover::after {
  transform: scale(1, 1);
}

</style>
