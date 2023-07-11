<template>
  <div id="app">
    <NavBar />
    <router-view />
    <FooterSocial />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import FooterSocial from './components/FooterSocial.vue';


export default {
  components: {
    NavBar,
    FooterSocial,

  }
}
</script>