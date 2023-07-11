<template>
    <div id="nav">
      <NavBar :use-router-link="false" />
    </div>
  </template>
  
  <script>
  import NavBar from './components/NavBar.vue';
  
  export default {
    components: {
      NavBar
    }
  }
  </script>