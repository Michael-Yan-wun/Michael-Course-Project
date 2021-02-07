<template>
  <div id="back-end">
    <!-- 整個table -->
    <div class="content">
      <h1>Michael小教室後台管理系統</h1>
      <input id="text-search" placeholder="Type to find..." type="search" />
      <!-- 整個table -->
      <table id="data-table">
        <thead>
          <tr>
            <th title="Field #1">id</th>
            <th title="Field #2">first_name</th>
            <th title="Field #3">last_name</th>
            <th title="Field #4">email</th>
            <th title="Field #5">gender</th>
            <th title="Field #6">ip_address</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Susanna</td>
            <td>Raffon</td>
            <td>sraffon0@gnu.org</td>
            <td>Female</td>
            <td>156.182.65.36</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "COURSEA000",
  data() {
    return {};
  }
};
</script>

<style scoped>
.content {
  max-width: 90%;
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
  text-align: left;
}

tr {
  transition: opacity 0.5s ease;
}
tr.hide {
  opacity: 0;
  height: 0;
}

td {
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
</style>
