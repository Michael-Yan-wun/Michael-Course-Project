<template>
  <swiper class="swiper container" :options="swiperOption">
    <swiper-slide v-for="i in 10" :key="i">
      <div id="couseCard" class="container">
        <div class="eachdiv">
          <img src="../assets/img/logo.png" />
          <h3>michael</h3>
          <h5>hello</h5>
          <p>
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptates
            ducimus eveniet beatae consequatur consequuntur. Incidunt ad porro
            provident ea facere nesciunt alias quasi doloremque illo, qui sequi
            architecto obcaecati odio.
          </p>
        </div>
      </div>
    </swiper-slide>
    <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
</template>

<script>
import { swiper, swiperSlide } from "vue-awesome-swiper";
import "swiper/swiper-bundle.css";

export default {
  name: "swiper-example-free-mode",
  title: "Free mode / No fixed positions",
  components: {
    swiper,
    swiperSlide
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 30,
        freeMode: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        }
      }
    };
  }
};
</script>
<style scoped>
.swiper {
  width: 100%;
  height: 625px;
}
.swiper.container {
  opacity: 0.9;
  background-image: url("../assets/img/library.jpeg");
  background-size: cover;
  border-radius: 15px;
  margin-bottom: 20px;
}

.swiper-slide {
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-sizing: border-box;
  padding: 0 80px;
  background-color: transparent;
    transform: scale(1.2);
}
.title {
  font-weight: bold;
}
.text {
  max-width: 430px;
  line-height: 1.32;
  margin-bottom: 280px;
}

.eachdiv {
  display: inline-table;
  width: 250px;
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
  /* color: #e91e63; */
  color: rgb(119, 126, 231);
  margin-bottom: 0.5rem;
}
/*styling card description*/
.eachdiv p {
  font-size: 0.8rem;
  color: #969696;
  margin-bottom: 0;
}
</style>
