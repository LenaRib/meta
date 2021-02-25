<template>
  <div id="app">
    <h1 class="title">Психотерапевты</h1>

    <hr>

      <table align="center" width="600" v-for="t in therapist" v-bind:key="t.id">
        <tr >
          <td width="100"><img
            v-bind:src="t.photo"
            width="51"
            height="68"></td>
          <td align="left" width="500">
            <tr>{{ t.name }}</tr>
            <tr>Методы: {{ t.metod }}</tr>
          </td>
        </tr>
      </table>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: "App",
  data () {
    return {
      therapist: [],
      name: '',
      photo: '',
      metod: '',
    }
  },
  mounted () {
    this.getTherapist()
  },
  methods: {
    getTherapist() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/therapist',
        auth: {
          username: 'lenarib',
          password: '21',
        }
      }).then(response => this.therapist = response.data )
    }
  } 
};
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
