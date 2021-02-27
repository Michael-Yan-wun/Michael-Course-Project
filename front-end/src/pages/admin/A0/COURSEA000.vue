<template>
  <div id="back-end">
    <loading :active.sync="isLoading"
      ><img src="../../../assets/img/loading.gif" alt="loading"
    /></loading>
    <!-- Input form -->
    <div>
      <b-card class="container" bg-variant="light">
        <h2 id="input-title"><u>Welcome to Michael's Studio</u></h2>
        <!-- 預覽卡片區 -->
        <h6 id="card-view">課程預覽-></h6>
        <b-card
          :title="courseDetails.name"
          img-src="https://picsum.photos/600/300/?image=25"
          tag="article"
          style="max-width: 18rem;"
          class="mb-2 left-card"
        >
          <b-card-text>
            講師: {{ courseDetails.teacher }} <br />
            地區: {{ courseDetails.loc }}<br />
            日期: {{ courseDetails.date }}<br />
            簡述: {{ courseDetails.content }}
          </b-card-text>
        </b-card>
        <b-form-group
          label="課程名稱："
          label-for="course-name"
          label-cols-sm="7"
          label-align-sm="right"
          valid-feedback="ok!"
          :invalid-feedback="cnameInvaild"
          :state="cnameState"
        >
          <b-form-input
            :state="cnameState"
            v-model="courseDetails.name"
            placeholder="Course Name"
            id="course-name"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          label="課程講師："
          label-for="course-teacher"
          label-cols-sm="7"
          label-align-sm="right"
          :invalid-feedback="tInvaild"
          :state="tState"
        >
          <b-form-input
            :state="tState"
            v-model="courseDetails.teacher"
            placeholder="Teacher's name"
            id="course-teacher"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          label="課程簡述："
          label-for="course-title"
          label-cols-sm="7"
          label-align-sm="right"
          :invalid-feedback="decInvaild"
          :state="decState"
        >
          <b-form-input
            :state="decState"
            v-model="courseDetails.content"
            placeholder="Course title"
            id="course-title"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          label="開課日期："
          label-for="course-content"
          label-cols-sm="7"
          label-align-sm="right"
        >
          <b-form-datepicker
            v-model="courseDetails.date"
            id="course-content"
            class="mb-2"
          ></b-form-datepicker>
        </b-form-group>

        <b-form-group
          label="上課地區："
          label-cols-sm="7"
          label-align-sm="right"
          class="mb-0"
          v-slot="{ region }"
        >
          <b-form-radio-group
            v-model="courseDetails.loc"
            class="pt-2"
            :options="['台北', '桃園', '台中']"
            :aria-describedby="region"
          ></b-form-radio-group>
        </b-form-group>
        <b-form-group
          id="course-img-label"
          class="mb-0"
          label="課程圖片："
          label-for="course-img"
          label-cols-sm="7"
          label-align-sm="right"
        >
          <b-form-file
            id="course-img"
            v-model="courseDetails.img"
            accept="image/*"
            placeholder="請選擇圖片檔(大小270x140)"
            drop-placeholder="Drop file here..."
          ></b-form-file>
        </b-form-group>
        <!-- button區域 -->
        <button id="add" @click="add">新增</button>
      </b-card>
    </div>

    <!-- 整個table -->
    <div class="content">
      <h1>Michael's Studio後台管理系統</h1>
      <!-- 整個table -->
      <table id="data-table">
        <thead>
          <tr>
            <th title="Field #1">上架與否</th>
            <th title="Field #2">課程編號</th>
            <th title="Field #3">課程名稱</th>
            <th title="Field #4">課程講師</th>
            <th title="Field #5">開課日期</th>
            <th title="Field #6">上課區域</th>
            <th title="Field #7">課程簡述</th>
            <th title="Field #8">操作按鈕</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in tableDetails" :key="index">
            <td>
              <input
                type="checkbox"
                id="online"
                :checked="item.online"
                @click="onlineChange(item)"
              />
            </td>
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.teacher }}</td>
            <td>{{ item.date }}</td>
            <td>{{ item.loc }}</td>
            <td>{{ item.content.substring(0, 10) + "......" }}</td>
            <td>
              <!-- 操作按鈕 -->
              <b-button
                variant="outline-info"
                @click="showModal_Modify(index)"
                ref="btnShow_modify"
                >Modify</b-button
              >
              <b-button
                variant="outline-danger"
                @click="showModal(index)"
                ref="btnShow"
                >Delete</b-button
              >
            </td>
            <!-- delete Modal -->
            <div>
              <b-modal
                :id="'delete-modal' + index"
                title="刪除確認"
                @ok="remove(index)"
              >
                <p class="my-4">是否刪除本資料</p>
              </b-modal>
            </div>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- modify Modal內容 -->
    <div>
      <b-modal
        v-for="(item, index) in modifyDetials"
        :key="index"
        :id="'modify-modal' + index"
        scrollable
        title="修改資料"
        @ok="modify(item)"
      >
        <div class="container ">
          <b-form-group
            label="課程名稱："
            label-for="modify-course-name"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input
              v-model="item.name"
              placeholder="Course Name"
              id="modify-course-name"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            label="課程講師："
            label-for="modify-course-teacher"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input
              v-model="item.teacher"
              placeholder="Teacher's name"
              id="modify-course-teacher"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            label="課程簡述："
            label-for="modify-course-title"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input
              v-model="item.content"
              placeholder="Course title"
              id="modify-course-title"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            label="開課日期："
            label-for="modify-course-content"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-datepicker
              v-model="item.date"
              id="modify-course-content"
              class="mb-2"
            ></b-form-datepicker>
          </b-form-group>

          <b-form-group
            label="上課地區："
            label-cols-sm="3"
            label-align-sm="right"
            class="mb-0"
            v-slot="{ loc }"
          >
            <b-form-radio-group
              v-model="item.loc"
              class="pt-2"
              :options="['台北', '桃園', '台中']"
              :aria-describedby="loc"
            ></b-form-radio-group>
          </b-form-group>
          <b-form-group
            id="course-img-label"
            class="mb-0"
            label="課程圖片："
            label-for="course-img"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <img class="courseImg" :src="item.img" />
          </b-form-group>
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { getAPI } from "../../../service";

export default {
  name: "COURSEA000",

  data() {
    return {
      // 新增至資料庫
      courseDetails: {
        name: "",
        teacher: "",
        loc: "",
        content: "",
        date: "",
        img: null,
        online: false
      },
      // 資料庫噴回來
      tableDetails: [
        // {
        //   id:'1',
        //   name:'Java',
        //   teacher:'michael',
        //   loc:'台中',
        //   date:'2020-12-14',
        //   content:'hello',
        //   online:true,
        //   img:null,
        //   sys:1
        // },
        //  {
        //   id:'2',
        //   name:'Python',
        //   teacher:'michael',
        //   loc:'台中',
        //   date:'2020-12-14',
        //   content:'hello',
        //   online:true,
        //   img:null,
        //   sys:1
        // },
      ],
      // 修改暫存區
      modifyDetials: [],
      //Loading
      isLoading: false
    };
  },

  created() {
    this.queryAllDatas();
    console.log(this.$store.state.username)
  },

  methods: {
    queryAllDatas() {
      getAPI("/api/course/details").then(response => {
        response.data.forEach(element => {
          if (element.sys == 1) {
            element.img = `http://127.0.0.1:8000${element.img}`;
            this.tableDetails.push(element);
            let copy = Object.assign({}, element);
            this.modifyDetials.push(copy);
          }
        });
        console.log(this.tableDetails);
        console.log(this.modifyDetials);
        this.isLoading = false;
      });
    },
    async add() {
      if (
        this.cnameState == true &&
        this.tState == true &&
        this.decState == true
      ) {
        // 包裝form-data 因為有file格式上傳
        let formData = new FormData();
        formData.append("name", this.courseDetails.name);
        formData.append("teacher", this.courseDetails.teacher);
        formData.append("loc", this.courseDetails.loc);
        formData.append("content", this.courseDetails.content);
        formData.append("date", this.courseDetails.date);
        formData.append("img", this.courseDetails.img);
        formData.append("online", this.courseDetails.online);
        formData.append("sys", 1);

        await axios
          .post("http://127.0.0.1:8000/api/course", formData, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`
            }
          })
          .then(response => {
            console.log(response);
            // refresh table
            this.modifyDetials=[];
            this.tableDetails = [];
            this.queryAllDatas();
            // clear input
            this.courseDetails = {
              name: "",
              teacher: "",
              loc: "",
              content: "",
              date: "",
              img: null,
              online: false
            };
            // add successful toast
            this.$bvToast.toast("新增成功", {
              title: "新增",
              variant: "success",
              solid: true
            });
          });
      } else {
        this.$bvToast.toast("請填寫必填欄位", {
          title: "新增失敗",
          variant: "danger",
          solid: true
        });
      }
    },

    async modify(item) {
      axios
        .put(`http://127.0.0.1:8000/api/course/${item.id}`, item, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`
          }
        })
        .then(response => {
          // console.log(response.status);
          if (response.status == 200) {
            this.$bvToast.toast("更新成功", {
              title: "更新訊息",
              variant: "info",
              solid: true
            });
            this.modifyDetials = [];
            this.tableDetails = [];
            this.queryAllDatas();
          } else {
            this.$bvToast.toast("更新失敗", {
              title: "更新訊息",
              variant: "warning",
              solid: true
            });
          }
        });
    },

    // soft-Delete
    async remove(index) {
      let id = this.tableDetails[index].id;
      await axios
        .delete(`http://127.0.0.1:8000/api/course/${id}`, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`
          }
        })
        .then(() => {
          this.tableDetails.splice(index, 1);
        })
        .catch(() => {
          this.$bvToast.toast("權限不足，刪除失敗", {
            title: "刪除訊息",
            variant: "danger",
            solid: true
          });
        });
    },

    // 控制Modal的項目
    // Delete
    showModal(value) {
      this.$root.$emit("bv::show::modal", "delete-modal" + value, "#btnShow");
    },
    // Modify
    showModal_Modify(value) {
      console.log(value);
      // 跳出Modal
      this.$root.$emit(
        "bv::show::modal",
        "modify-modal" + value,
        "#btnShow_modify"
      );
    },
    //checkbox的狀態
    async onlineChange(item) {
      let id = item.id;
      item.online = !item.online;
      await axios
        .put(
          `http://127.0.0.1:8000/api/course/online/${id}`,
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`
            }
          },
          item
        )
        .then(() => {
          if (item.online == true) {
            this.$bvToast.toast("上架成功", {
              title: "上架資訊",
              variant: "info",
              solid: true
            });
          } else {
            this.$bvToast.toast("下架成功", {
              title: "上架資訊",
              variant: "info",
              solid: true
            });
          }
        });
    }
  },
  // 欄位驗證使用
  computed: {
    APIData() {
      return this.$store.state.APIData;
    },
    // 課程名稱
    cnameState() {
      return (
        this.courseDetails.name.length != 0 &&
        this.courseDetails.name != "" &&
        this.courseDetails.name != null
      );
    },
    cnameInvaild() {
      if (this.courseDetails.name.length == 0) {
        return "請輸入課程名稱!";
      }
    },
    // 課程講師
    tState() {
      return (
        this.courseDetails.teacher.length != 0 &&
        this.courseDetails.teacher != "" &&
        this.courseDetails.teacher != null
      );
    },
    tInvaild() {
      if (this.courseDetails.teacher.length == 0) {
        return "請輸入老師名稱!";
      }
    },
    // 課程簡述
    decState() {
      return (
        this.courseDetails.content.length >= 10 &&
        this.courseDetails.content != "" &&
        this.courseDetails.content != null
      );
    },
    decInvaild() {
      if (this.courseDetails.content.length > 0) {
        return "輸入最少10個字!";
      }
      return "請輸入課程簡述!";
    }
  }
};
</script>

<style scoped>
* {
  color: #34495e;
  font-family: Georgia, "Times New Roman", Times, serif;
}

/* loading css */
#loading {
  opacity: 0.8;
}

/* input css */
.container {
  max-width: 85%;
  margin-top: 20px;
  position: relative;
}
#input-title {
  text-align: center;
  margin-bottom: 30px;
}

#course-img,
#course-img-label {
  margin-top: 10px;
}

#add {
  width: 200px;
  border: solid;
  border-radius: 25px;
  background-color: bisque;
  float: right;
  margin: 20px 10px 0px 10px;
  right: 30px;
  bottom: 10px;
}

#card-view {
  position: absolute;
  margin: 0px 0px 0px 45px;
}

/* left-card css */
.left-card {
  position: absolute;
  margin: 0px 20px 20px 130px;
}

/* table css */
.content {
  max-width: 85%;
  margin: 50px auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  text-transform: uppercase;
  border-bottom: 1px solid #0e0e0e;
}
thead th {
  padding: 5px;
  text-align: center;
}

td {
  text-align: center;
  padding: 5px;
  border-bottom: 1px solid #d6d6d6;
}

tr:hover td {
  background: #e6e6e6;
}

#text-search {
  max-width: 240px;
  display: block;
  width: 100%;
  height: 44px;
  padding: 0 10px;
  margin: 0;
  border: 1px solid #cccccc;
  outline: none;
  color: #5f6a7d;
  font: 13px;
  font-family: "Nunito", sans-serif;
  font-weight: 100;
  margin-bottom: 15px;
  float: right;
}

#data-table {
  border: solid 2px;
}

/* modal彈出的image */
.courseImg {
  margin-top: 15px;
  width: 270px;
  height: 140px;
}
</style>
