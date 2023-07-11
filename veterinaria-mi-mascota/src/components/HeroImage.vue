<template>
    <div class="hero-image">
      <div class="hero-text">
        <h1>Veterinaria Mi Mascota</h1>
      </div>
    </div>
</template>
  
  <script>
  export default {
    // Component options
  }
  </script>
  
  <style scoped>
  .hero-image {
  position: relative;
  height: 100vh;
  background-image: url("../assets/hero.jpg");
  background-size: cover;
}

.hero-image::before {
 
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* color semi-transparente */
}

.hero-text {
  font-size: 1.6rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* agregar sombra al texto */
  color: #fff;
  font-weight: bold;
  white-space: nowrap; /* para que el texto no se divida en dos líneas */
}

@media only screen and (min-width: 768px) and (max-width: 1024px) {
  
.hero-text {
  font-size: 22px;
}
}

@media screen and (max-width: 768px) {
  .hero-image{
    background-image: url("../assets/hero-m2.png");
  }
  .hero-text {
    font-size: 1.2rem !important;
    white-space: normal;
  }
}
  </style>
  