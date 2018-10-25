<template>
  <div>
    Vue SocketIO Test
    <p />
    <button @click="onSendMsgBtn">send 'hello world!'</button>
    <button @click="onSnedMsgBtn2">get 'hello'</button>
    <button @click="runTask">run backend task</button><br>
    <br>
    <div v-for="(message, index) in messages" :key="index">
      {{ message }}
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'Index',

  data() {
    return {
      messages: []
    }
  },

  sockets: {
    connect() {
      console.log('socket connected')
    },
    data(val) {
      console.log('This method was fired by the socket server. eg: io.emit("data", data)')
      console.log(val)
      // alert(val.data)
      this.messages.push('Received: ' + val.data)
    },
    disconnect() {
      console.log('socket disconnect')
    },
  }, // sockets

  methods: {
    onSendMsgBtn() {
      // $socket is socket.io-client instance
      this.$socket.emit('data', { 'data': 'Hello world!' })
    },
    onSnedMsgBtn2() {
      axios.post('http://' + location.hostname + ':5000' + '/send').then(res => {
        console.log(res)
      })
    },
    runTask() {
      axios.post('http://' + location.hostname + ':5000' + '/task').then(res => {
        console.log(res)
      })
    }
  } // methods
}
</script>
