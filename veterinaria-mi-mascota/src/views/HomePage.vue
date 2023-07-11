<template>
    <div>
      <HeroImage />
      <LandingIni />
    </div>
</template>
  
  <script>
  import HeroImage from '../components/HeroImage.vue';
  import LandingIni from '../components/LandingIni.vue';
  
  export default {
    name: 'HomePage',
    components: {
      HeroImage,
      LandingIni
    }
  }
  </script>
  