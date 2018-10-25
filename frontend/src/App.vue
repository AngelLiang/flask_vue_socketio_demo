<template>
  <div id="app">
    <img src="./assets/logo.png">
    <Index />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import Index from './views/Index'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Index
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
