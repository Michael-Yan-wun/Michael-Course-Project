<!-- 
程式：FARMA000.vue
功能：後台記帳區
作者：林彥文
完成：2020-12-09
-->
<template>
  <div>
    <el-container style="height:100vh ;border: 1px solid #eee">
      <el-aside>
        <el-menu :default-openeds="['1']">
          <el-submenu index="0">
            <template slot="title"
              ><router-link :to="{ name: 'FARMA000' }"
                ><i class="el-icon-s-home"></i>回首頁</router-link
              >
            </template>
          </el-submenu>
          <el-submenu index="1">
            <template slot="title"
              ><router-link :to="{ name: 'FARMA100' }">
                <i class="el-icon-message"></i>銷售紀錄系統</router-link
              >
            </template>
            <!-- <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group> -->
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-container>
        <!-- 上方標題列 -->
        <el-header>
          <span>員工：林彥文</span>
        </el-header>
        <el-main>
          <!-- input form -->
          <div class="container">
            <b-card bg-variant="light">
              <b-form-group
                label-cols-lg="3"
                label="農農的愛-銷售紀錄系統"
                label-size="lg"
                label-class="font-weight-bold pt-0"
                class="mb-0"
              >
                <b-form-group
                  label-cols-sm="3"
                  label="銷售日期:"
                  label-align-sm="right"
                  label-for="salesdate"
                >
                  <b-form-input
                    id="salesdate"
                    type="date"
                    v-model="salesData.salesDate"
                    :state="salesDate_sts"
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  label-cols-sm="3"
                  label="銷售區域:"
                  label-align-sm="right"
                  label-for="location"
                >
                  <b-form-select
                    v-model="salesData.location"
                    :options="region"
                    :state="location_sts"
                  ></b-form-select>
                </b-form-group>

                <b-form-group
                  label-cols-sm="3"
                  label="銷售物品:"
                  label-align-sm="right"
                  label-for="item"
                >
                  <b-form-select
                    v-model="salesData.item"
                    :options="items"
                    :state="item_sts"
                  ></b-form-select>
                </b-form-group>

                <b-form-group
                  label-cols-sm="3"
                  label="銷售單價:"
                  label-align-sm="right"
                  label-for="price_each"
                >
                  <b-form-input
                    :state="price_each_sts"
                    id="price_each"
                    v-model="salesData.price_each"
                    aria-describedby="price"
                  ></b-form-input>
                  <b-form-invalid-feedback id="price">
                    請輸入非零的數字
                  </b-form-invalid-feedback>
                </b-form-group>
                <b-form-group
                  label-cols-sm="3"
                  label="銷售數量(斤):"
                  label-align-sm="right"
                  label-for="number"
                >
                  <b-form-input
                    id="numbers"
                    :state="number_sts"
                    aria-describedby="number"
                    v-model="salesData.number"
                  ></b-form-input>
                  <b-form-invalid-feedback id="number">
                    請輸入非零的數字
                  </b-form-invalid-feedback>
                </b-form-group>
              </b-form-group>
              <b-button
                type="button"
                class="inputbtn"
                pill
                variant="outline-primary"
                @click="save()"
                >全部存檔</b-button
              >
              <b-button
                type="button"
                class="inputbtn"
                pill
                variant="outline-warning"
                @click="reset()"
                >重置</b-button
              >
              <b-button
                type="button"
                class="inputbtn"
                pill
                variant="outline-success"
                @click="add()"
                >新增</b-button
              >
            </b-card>
          </div>
          <!--table相關  -->
          <el-table :data="detail" style="width: 100%">
            <el-table-column label="銷售日期" width="130">
              <template slot-scope="data">
                {{ data.row.salesDate }}
                <!-- <el-date-picker
                  class="input_date"
                  v-model="data.row.salesDate"
                  type="date"
                  placeholder="請選擇日期"
                  format="yyyy/MM/dd"
                  size="small"
                  align="left"
                >
                </el-date-picker> -->
              </template>
            </el-table-column>
            <el-table-column prop="sno" label="銷售編號" width="100">
            </el-table-column>
            <el-table-column label="銷售資料" width="auto">
              <el-table-column prop="name" label="姓名" width="100">
              </el-table-column>
              <el-table-column prop="dept" label="部門" width="100">
              </el-table-column>
              <el-table-column label="銷售明細">
                <!-- 銷售區域 -->
                <el-table-column label="銷售區域" width="120">
                  <template slot-scope="data">
                    <span v-if="data.row.sts == 'save'">
                      {{ data.row.location }}
                    </span>
                    <span v-else>
                      <el-select
                        v-model="data.row.location"
                        placeholder="請選擇"
                      >
                        <el-option
                          v-for="item in region"
                          :key="item.value"
                          :value="item.value"
                        >
                        </el-option>
                      </el-select>
                    </span>
                  </template>
                </el-table-column>

                <!-- 銷售物品 -->
                <el-table-column prop="item" label="物品" width="110">
                  <template slot-scope="data">
                    <span v-if="data.row.sts == 'save'">
                      {{ data.row.item }}
                    </span>
                    <span v-else>
                      <el-select v-model="data.row.item" placeholder="請選擇">
                        <el-option
                          v-for="item in items"
                          :key="item.value"
                          :value="item.value"
                        >
                        </el-option>
                      </el-select>
                    </span>
                  </template>
                </el-table-column>

                <!-- 單價 -->
                <el-table-column label="單價" width="100">
                  <template slot-scope="data">
                    <span v-if="data.row.sts == 'save'">
                      {{ data.row.price_each }}
                    </span>
                    <span v-else>
                      <el-input
                        v-model="data.row.price_each"
                        placeholder="輸入價格"
                      ></el-input>
                    </span>
                  </template>
                </el-table-column>

                <!-- 數量(斤) -->
                <el-table-column label="數量(斤)" width="100">
                  <template slot-scope="data">
                    <span v-if="data.row.sts == 'save'">
                      {{ data.row.number }}
                    </span>
                    <span v-else>
                      <el-input
                        v-model="data.row.number"
                        placeholder="輸入數量"
                      ></el-input>
                    </span>
                  </template>
                </el-table-column>

                <el-table-column label="總價" width="120">
                  <template slot-scope="data">
                    {{ data.row.number * data.row.price_each }}
                  </template>
                </el-table-column>
                <el-table-column
                  prop="updatetime"
                  label="更新日期"
                  width="auto"
                >
                </el-table-column>
                <el-table-column prop="ip" label="ip位置" width="120">
                </el-table-column>

                <el-table-column label="操作動作" width="200">
                  <template slot-scope="data">
                    <el-button
                      type="primary"
                      icon="el-icon-edit"
                      circle
                      @click="revise(data.row.sno)"
                    ></el-button>
                    <el-button
                      type="success"
                      icon="el-icon-check"
                      circle
                      @click="check(data.row.sno)"
                    ></el-button>
                    <el-button
                      type="danger"
                      icon="el-icon-delete"
                      circle
                      @click="remove(data.row.sno)"
                    ></el-button>
                  </template>
                </el-table-column>
              </el-table-column>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "FARMA000",
      //下方顯示欄位的detail
      detail: [
        {
          sts: "save",
          name: "林彥文",
          dept: "資訊部",
          location: "台中",
          item: "番茄",
          price_each: 150,
          number: 10,
          price_total: "",
          sno: "10",
          updatetime: "2020-12-14",
          salesDate: "2020-12-15",
          ip: "192.168.56.103"
        },
        {
          sts: "save",
          name: "李亮亨",
          dept: "業務部",
          location: "台北",
          item: "草莓",
          price_each: 160,
          number: 5,
          price_total: "",
          sno: "11",
          updatetime: "2020-12-14",
          salesDate: "2020-08-15",
          ip: "10.15.56.106"
        }
      ],
      salesData: {
        location: "",
        item: "",
        price_each: "",
        number: null,
        salesDate: ""
      },
      region: [
        { value: "台中", text: "台中" },
        { value: "台北", text: "台北" }
      ],
      items: [
        { value: "番茄", text: "番茄" },
        { value: "草莓", text: "草莓" }
      ]
    };
  },
  methods: {
    // 新增銷售紀錄
    add() {
      if (
        this.price_each_sts &&
        this.number_sts &&
        this.item_sts &&
        this.salesDate_sts &&
        this.location_sts
      ) {
        //預設sts為儲存的狀態
        this.salesData.sts = "save";
        this.detail.push(this.salesData);
        this.salesData = {
          location: "",
          item: "",
          price_each: "",
          number: null,
          salesDate: ""
        };
      } else {
        const variant = variant;
        this.$bvToast.toast("請填完所有項目", {
          title: `新增 ${variant || "警告"}`,
          variant: "danger",
          solid: true
        });
      }
    },
    // 儲存全部資料進資料庫
    save() {
      console.log(this.detail);
    },
    //重置所有input欄位
    reset() {
      this.salesData = {
        location: "",
        item: "",
        price_each: "",
        number: null,
        salesDate: ""
      };
    },
    //刪除該欄位
    remove(sno) {
      this.detail.forEach(item => {
        if (item.sno == sno) {
          this.detail.pop(item);
        }
      });
    },
    //修改
    revise(sno) {
      this.detail.forEach(item => {
        if (item.sno == sno) {
          item.sts = "modify";
        }
      });
    },
    check(sno) {
      this.detail.forEach(item => {
        if (item.sno == sno) {
          item.sts = "save";
        }
      });
    }
  },
  computed: {
    price_each_sts() {
      const regex = /^(0|[1-9][0-9]*)$/;
      return regex.test(this.salesData.price_each);
    },
    number_sts() {
      const regex = /^(0|[1-9][0-9]*)$/;
      return regex.test(this.salesData.number);
    },
    item_sts() {
      const regex = /^[\u4E00-\u9FA5A-Za-z0-9_]+$/;
      return regex.test(this.salesData.item);
    },
    salesDate_sts() {
      return this.salesData.salesDate != "";
    },
    location_sts() {
      const regex = /^[\u4E00-\u9FA5A-Za-z0-9_]+$/;
      return regex.test(this.salesData.location);
    }
  }
};
</script>

<style scoped>
/* 按鈕間隔 */
.inputbtn {
  float: right;
  margin-right: 10px;
}

.el-header {
  background-color: rgb(172, 207, 168);
  color: #333;
  line-height: 60px;
  text-align: right;
  font-size: 12px;
}

.container {
  float: left;
  margin-bottom: 20px;
}

.el-aside {
  width: 200px !important ;
  background-color: rgb(238, 241, 246);
}
</style>
