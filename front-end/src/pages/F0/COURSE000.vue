<template>
  <div>
    <Header/>
    <!-- 說明區 -->
    <Intro />
    <!-- 精選書籍 -->
    <div class="container">
      <h2 class="Title">精選書籍</h2>
      <h4 class="subTitle">Michael哥親自為您挑選必讀書籍</h4>
      <div class="recommendPage">
        <swiper :options="swiperOption" ref="mySwiper">
          <swiper-slide v-for="(item, index) in books" :key="index"
            ><img class="books" :src="item"
          /></swiper-slide>

          <div class="swiper-pagination" slot="pagination"></div>
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>
    </div>
    <!-- 課程卡片區 -->
    <div id="couseCard" class="container">
      <h2 class="Title">華麗課程</h2>
      <h4 class="subTitle">
        專業團隊老師，從<span style="color:red;font-weight:bolder">零</span
        >變<span style="font-weight:bolder">大師</span>
      </h4>
      <div class="eachdiv" v-for="(item, index) in details" :key="index">
        <img :src="item.img" />
        <h3>{{ item.name }}</h3>
        <h5>{{ item.teacher }}</h5>
        <h5>{{ item.date }}</h5>
        <p>{{ item.content }}</p>
      </div>
    </div>
    <div>
      <h2 class="studentTitle">同學我有話要說</h2>
      <Student/>
    </div>
    <Footer id="footer" />
  </div>
</template>

<script>
import Intro from "../../components/introSwiper";
import Student from "../../components/student";
import { swiper, swiperSlide } from "vue-awesome-swiper";
import "swiper/swiper-bundle.css";

import Footer from "@/components/Footer.vue";
import axios from "axios";
import Header from '../../components/Header'

export default {
  name: "COURSE000",
  components: {
    Header,
    Footer,
    swiper,
    swiperSlide,
    Intro,
    Student
  },
  data() {
    return {
      details: [],
      books: [
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/084/60/0010846042.jpg&w=374&h=374&v=5e131a47",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/088/12/0010881286.jpg&w=374&h=374&v=5ffc28af",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/084/77/0010847790.jpg&w=374&h=374&v=5e203b3d",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/088/33/0010883365.jpg&w=374&h=374&v=601140b9",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/85/0010878564.jpg&w=374&h=374&v=5fcf55c1",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/081/23/0010812394.jpg&w=374&h=374&v=5c41aad0",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/088/15/0010881571.jpg&w=374&h=374&v=5ffed9c0",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/18/0010871876.jpg&w=374&h=374&v=5f6b23bc",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/94/0010879493.jpg&w=374&h=374&v=5fdc84b1",
        "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/57/0010875789.jpg&w=374&h=374&v=5fb3b441"
      ],
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 30,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
          dynamicBullets: true
        },
        loop: true,
        autoplay: {
          delay: 10000,
          stopOnLastSlide: false,
          disableOnInteraction: false
        },
        // // 显示分页
        // pagination: {
        //   el: ".swiper-pagination",
        //   clickable: true //允许分页点击跳转
        // },
        // // 设置点击箭头
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      }
    };
  },
  created() {
    this.fetchAllDatas();
  },
  mounted() {
    console.log("Current Swiper instance object", this.mySwiper);
    // this.mySwiper.slideTo(3, 1000, false);
  },
  methods: {
    fetchAllDatas() {
      axios.get("http://127.0.0.1:8000/api/course/details").then(response => {
        response.data.forEach(element => {
          if (element.sys == 1) {
            element.img = `http://127.0.0.1:8000${element.img}`;
            this.details.push(element);
          }
        });
      });
    }
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.swiper;
    }
  }
};
</script>
<style scoped>
* {
  font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN",
    "Hiragino Sans", Meiryo, sans-serif;
  color: rgba(0, 0, 0, 0.65);
}

/* footer css */
#footer {
  /* margin-top: 100px; */
  /* border: rgb(0, 190, 164) solid 2px; */
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

#intro {
  margin-bottom: 15px;
  background-color: gray;
  width: 100%;
  height: 200px;
}

#styleSwiper {
  /* margin: 20px; */
  width: 300px;
  height: 400px;
  margin-bottom: 20px;
}


.Title {
  position: relative;
  text-align: center;
  padding-top: 15px;
  color: rgb(0, 190, 164);
  font-weight: bolder;
}
.subTitle {
  position: relative;
  text-align: center;
  padding-top: 10px;
  color: rgba(0, 0, 0, 0.65);
}

.cards {
  margin: 20px;
  display: inline-table;
  height: 200px;
  width: 250px;
  box-shadow: 0 4px 16 px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}
.cards > img {
  height: inherit;
  width: inherit;
}

/* On mouse-over, add a deeper shadow */
.cards:hover {
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

/* swiper css */
.recommendPage .swiper-container {
  position: relative;
  width: 100%;
  height: 350px;
  padding-bottom: 50px;
}
.recommendPage .swiper-container .swiper-slide {
  width: 100%;
  line-height: 200px;
  text-align: center;
  padding-bottom: 150px;
}
.books {
  /* box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2); */
  transform: scale(0.7);
  margin-bottom: 20px;
}

/*styling the each card*/
.eachdiv {
  display: inline-table;
  width: 23.5%;
  background: white;
  box-shadow: 1px 2px 10px #33333352;
  padding: 1rem;
  margin: 0.5rem 0.4%;
  border-radius: 1rem;
  cursor: pointer;
  transition: 0.4s;
}
/*card Hover State*/
.eachdiv:hover {
  transform: scale(1.03);
  box-shadow: 2px 6px 10px #2f2f2f69;
}
/*styling the card images*/
.eachdiv img {
  width: 100%;
  margin-bottom: 0.8rem;
  border-radius: 1rem;
}
/*styling card title*/
.eachdiv h3 {
  color: #e91e63;
  /* color: rgb(0, 190, 164); */
  margin-bottom: 0.5rem;
}
/*styling card description*/
.eachdiv p {
  font-size: 0.8rem;
  color: #969696;
  margin-bottom: 0;
}

.swiper-button-prev,
.swiper-button-next {
  color: rgb(0, 190, 164);
}
.swiper-button-prev:hover {
  transform: scale(1.2);
}

.studentTitle{
  margin-left: 30px;
  margin-top: 30px;
  color: rgb(0, 190, 164);
}
</style>
