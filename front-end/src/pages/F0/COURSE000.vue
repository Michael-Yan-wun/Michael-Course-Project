<template>
  <div id="whole">
    <!-- 說明區 -->
    <div id="intro"></div>
    <!-- 精選書籍 -->
    <div v-swiper:mySwiper="swiperOption" id="styleSwiper">
      <div class="swiper-wrapper">
        <div class="swiper-slide" :key="banner" v-for="banner in banners">
          <img :src="banner" />
        </div>
      </div>
      <div class="swiper-pagination"></div>
    </div>
    <!-- 卡片區 -->
    <div class="mycard">
      <div class="card" v-for="(item, index) in details" :key="index">
        <img :src="item.courseImg" alt="Avatar" style="width:100%" />
        <div class="container">
          <h5>
            <b>{{ item.title }}</b>
          </h5>
          <p>{{ item.desc }}</p>
        </div>
      </div>
    </div>
    <Footer id="footer" />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
  name: "COURSE000",
  components: {
    Footer
  },
  mounted() {
    console.log("Current Swiper instance object", this.mySwiper);
    this.mySwiper.slideTo(3, 1000, false);
  },
  data() {
    return {
      details: [
        {
          title: "Python資料科學",
          desc: "用Python帶你探索大數據的秘境",
          courseImg:
            "https://exfast.me/wp-content/uploads/2019/04/1554182762-cddf42691119d44059a16a4095047a33-1140x600.jpg"
        },
        {
          title: "Java班",
          desc: "用途最廣的Java等你來挑戰",
          courseImg:
            "https://exfast.me/wp-content/uploads/2019/04/1554182762-cddf42691119d44059a16a4095047a33-1140x600.jpg"
        }
      ],
      banners: [
        "https://exfast.me/wp-content/uploads/2019/04/1554182762-cddf42691119d44059a16a4095047a33-1140x600.jpg",
        "https://exfast.me/wp-content/uploads/2019/04/1554182762-cddf42691119d44059a16a4095047a33-1140x600.jpg",
        "https://exfast.me/wp-content/uploads/2019/04/1554182762-cddf42691119d44059a16a4095047a33-1140x600.jpg"
      ],
      swiperOption: {
        pagination: {
          el: ".swiper-pagination"
        }
      }
    };
  },
  methods: {}
};
</script>
<style scoped>
#footer {
  margin-top: 100px;
  padding-top: 50px;
  position: relative;
  bottom: 0;
  height: 240px;
  background-color: rgb(237, 237, 237);
  width: 100vw;
  padding: 0;
  font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN",
    "Hiragino Sans", Meiryo, sans-serif;
}

#whole{
  background-color: rgb(207, 205, 205);
}

#intro {
  margin-bottom: 15px;
  background-color: gray;
  width: 100%;
  height: 200px;
}

#styleSwiper{
  /* margin: 20px; */
  width: 300px;
  height: 300px;
}

.mycard{
  background-color: rgb(237, 237, 237);
}


.card {
  /* Add shadows to create the "card" effect */
  margin: 20px;
  display: inline-table;
  height: 250px;
  width: 300px;
  box-shadow: 0 4px 16 px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}
.card > img {
  height: inherit;
  width: inherit;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  right: 10px;
  bottom: 10px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 4px 16px;
}
.container.top {
  margin-bottom: 50px;
}
</style>
