<template>
  <main>
    <!-- Presentación de la página -->
    <section id="presentacion">
      <div class="contenedor-presentacion">
        <h2 class="presentacion-titulo">¡Bienvenidos!</h2>
        <p class="presentacion-parrafo">
          En nuestra clínica veterinaria contamos con un equipo de profesionales altamente capacitados para atender a tus mascotas con los mejores cuidados y servicios. También contamos con un Pet Shop completo para darle amor y estilo a tu mascota.
        </p>
        <div class="presentacion-imagenes">
          <div class="presentacion-imagen">
            <img src="../assets/vet1.jpg" alt="Imagen 1">
          </div>
          <div class="presentacion-imagen">
            <img src="../assets/vet2.jpg" alt="Imagen 2">
          </div>
          <div class="presentacion-imagen">
            <img src="../assets/vet3.jpg" alt="Imagen 3">
          </div>
        </div>
      </div>
    </section>

    <!-- Sección Descriptiva de vocación y servicios -->

    <section class="clinica">
      <div class="fondo-clinica"></div>
      <div class="contenedor-clinica">
        <div class="columna-clinica">
          <div class="cabecera-imagen"></div>
          <h3 class="sub-clinica">Amor Animal</h3>
          <p class="parrafo-clinica">
            En nuestra clínica veterinaria, nos apasiona brindar la mejor atención posible a tus mascotas. Nuestro equipo de profesionales está dedicado a garantizar que tus amigos peludos reciban el cuidado y el amor que merecen.          </p>
        </div>
        <div class="columna-clinica">
          <div class="cabecera-imagen"></div>
          <h3 class="sub-clinica">Nuestros Servicios</h3>
          <p class="parrafo-clinica">
            Ofrecemos una amplia gama de servicios para mantener a tus mascotas saludables y felices. Desde atención preventiva hasta tratamiento de enfermedades, nuestro equipo está aquí para ayudarte a cuidar de tus amigos peludos.
          </p>
        </div>
      </div>
    </section>

    <!-- Sección Pet-shop -->

    <section id="pet-shop">
      <h2>Pet Shop</h2>
      <div class="carousel-container">
        <ul class="carousel-slide">
          <li><router-link to="/PetShopPage"><img src="../assets/slide1.jpg" alt="Imagen 1"></router-link></li>
          <li><router-link to="/PetShopPage"><img src="../assets/slide2.jpg" alt="Imagen 2"></router-link></li>
          <li><router-link to="/PetShopPage"><img src="../assets/slide3.jpg" alt="Imagen 3"></router-link></li>
          <li><router-link to="/PetShopPage"><img src="../assets/slide4.jpg" alt="Imagen 4"></router-link></li>
        </ul>
        <a class="carousel-prev" @click="prevSlide">&#10094;</a>
        <a class="carousel-next" @click="nextSlide">&#10095;</a>
        <div class="carousel-dots-container">
          <div class="carousel-dots">
            <span class="carousel-dot"></span>
            <span class="carousel-dot"></span>
            <span class="carousel-dot"></span>
            <span class="carousel-dot"></span>
          </div>
        </div>
      </div>
    </section>

    <!-- Sección de contacto -->

    <section id="contacto">
      <div class="video-container">
        <iframe id="video" :src="videoSrc" frameborder="0" allowfullscreen></iframe>
        <div class="video-overlay"></div>
      </div>
      <div class="contenedor-contacto">
        <h2 class="titulo-contacto"><router-link to="/ContactoPage">Contacto</router-link></h2>
        <div class="contiene-info-mapa">
          <div class="informacion-contacto">
            <ul>
              <li><i class="fas fa-map-marker-alt"></i> Av. Siempreviva 742</li>
              <li><i class="fas fa-phone"></i> +54 11 5555-5555</li>
              <li><i class="fas fa-clock"></i> Horarios de atención: <br> Lunes a Viernes de 9:00 a 18:00, <br> Sábados de 9:00 a 13:00</li>
              <li><i class="fa-solid fa-truck-medical"></i> Emergencias: +54 11 5555-4444 (24/7)</li>
              <li><i class="fa-solid fa-map-location-dot"></i> Otras sucursales: Av. Libertad 1234, Córdoba</li>
              <li><i class="fas fa-envelope"></i> info@veterinariamascotera</li>
            </ul>
          </div>
          <div id="mapa">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3400.686870335936!2d-64.1876458494149!3d-31.416289267847355!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9423a31b9d1dcf8b%3A0x4cd4a4d896e87209!2sC%C3%B3rdoba%2C%20Provincia%20de%20C%C3%B3rdoba!5e0!3m2!1sen!2sar!4v1650535245367!5m2!1sen!2sar" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  data() {
    return {
      videoSrc: "https://www.youtube.com/embed/C---wF7YKtI?controls=0&showinfo=0&rel=0&autoplay=1&mute=1&loop=1&playlist=C---wF7YKtI",
      slideIndex: 0
    };
  },
  mounted() {
 
      this.showSlides();
      setInterval(this.showSlides, 3000);
      window.addEventListener("resize", this.setVideoSrc);
      this.setVideoSrc();
      this.animateElements();
  },
  methods: {
    
    showSlides() {
  const slides = document.querySelectorAll(".carousel-slide li");
  const dots = document.querySelectorAll(".carousel-dot");
  if (slides.length && dots.length) {
    for (let i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
      dots[i].classList.remove("active");
    }
    this.slideIndex++;
    if (this.slideIndex > slides.length) {
      this.slideIndex = 1;
    }
    slides[this.slideIndex - 1].style.display = "block";
    dots[this.slideIndex - 1].classList.add("active");
  }
},
animateElements() {
      const elementAnimation = [
        { transform: "translateY(-100px)", opacity: 0 },
        { transform: "translateY(0)", opacity: 1 },
      ];

      const elementTiming = {
        duration: 700,
        iterations: 1,
      };

      const navElements = document.querySelectorAll("nav *");
      const titleElement = document.querySelector(".hero-text h1");

      [...navElements, titleElement].forEach((element) => {
        element.animate(elementAnimation, elementTiming);
      });
    },
 
    prevSlide() {
      this.slideIndex--;
      this.showSlides();
    },
    nextSlide() {
      this.slideIndex++;
      this.showSlides();
    },
    setVideoSrc() {
      if (window.innerWidth < 600) {
        this.videoSrc = "https://www.youtube.com/embed/tIt82sUYvho?controls=0&showinfo=0&rel=0&autoplay=1&mute=1&loop=1&playlist=tIt82sUYvho";
      } else {
        this.videoSrc = "https://www.youtube.com/embed/C---wF7YKtI?controls=0&showinfo=0&rel=0&autoplay=1&mute=1&loop=1&playlist=C---wF7YKtI";
      }
    }
    
    

  }
};
</script>




<style>
#presentacion {
  background-color: #f5f5f5;
  padding: 6% 0;
}

.contenedor-presentacion {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.presentacion-titulo {
  font-size: 36px;
  color: #885ead;
  margin-bottom: 30px;
 
}




.presentacion-parrafo {
  font-size: 18px;
  line-height: 1.5;
  margin: 0 auto;
  margin-bottom: 3%;
  max-width: 60%;
}

.presentacion-imagenes {
  display: flex;
  justify-content: space-between;
}

.presentacion-imagen {
  flex-basis: calc(33.33% - 20px);

}

.presentacion-imagen img {
  width: 100%;
  height: 100%;
  border-radius: 3%;
  object-fit: cover;
}




/**************************** SECCIÓN CLINICA ***********/

/* Estilos generales */
.clinica {
  position: relative;
  margin-top: 50px;
  padding: 50px 0;
  background-image: url('../assets/service.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  color: #fff;
  text-align: center;
  z-index: -1;
}

/* Fondo antes de la imagen de fondo */
.clinica:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(17, 0, 255, 0.7);
  z-index: -2;
}

/* Contenedor de las columnas */
.contenedor-clinica {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  max-width: 1200px;
  margin: 0 auto;
  z-index: 1;
}

/* Columnas */
.columna-clinica {
  width: 45%;
  margin-bottom: 50px;
  transition: transform 0.3s ease;
}

.columna-clinica:hover {
  transform: translateY(-10px);
}

/* Imágenes de cabecera */
.cabecera-imagen {
  height: 100px;
  margin: 0 auto 20px auto;
  text-align: center;
}

.columna-clinica:nth-child(1) .cabecera-imagen {
  content: url('../assets/cabecera1.png');
}

.columna-clinica:nth-child(2) .cabecera-imagen {
  content: url('../assets/cabecera2.png');
}

/* Títulos */
.sub-clinica {
  font-size: 36px;
  margin-bottom: 20px;
  text-transform: uppercase;
  transition: color 0.3s ease;
}

.columna-clinica:hover h2 {
  color: #b2d9ea;
}

/* Párrafos */
.parrafo-clinica {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 20px;
  transition: color 0.3s ease;
}

.columna-clinica:hover p {
  color: #b2d9ea;
}

/***************************** SECCIÓN PET-SHOP **************/

#pet-shop {
  width: 100%;
  background-color: #fff;
  padding: 50px 0;
}

#pet-shop h2 {
  text-align: center;
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 40px;
  color: #885ead;
}

.carousel-container {
  position: relative;
  margin: 0 auto;
  width: 100%;
  overflow: hidden;
}

.carousel-slide {
  display: flex;
  width: 100%;
  overflow-x: auto;

  list-style: none;
  padding: 0;
  margin: 0;
}

.carousel-slide::-webkit-scrollbar {
  display: none;
}

.carousel-slide li {
  flex: 0 0 auto;
  width: 100%;
  height: 50%;
}

.carousel-slide img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.carousel-prev,
.carousel-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 4rem;
  color: #fff;
  cursor: pointer;
  z-index: 1;
}

.carousel-prev {
  left: 10px;
}

.carousel-next {
  right: 10px;
}

.carousel-dots-container {
  margin-top: 30px;
  text-align: center;
}

.carousel-dots {
  display: inline-block;
}

.carousel-dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.carousel-dot.active {
  background-color: black
}

/****************************** Sección de contacto */
#contacto {
  position: relative;
  background-color: #885ead;
  color: #fff;
  padding: 80px 0;
  z-index: 1;
}
.video-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
}

.video-container iframe {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
}
.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  background-color: rgba(0, 0, 0, 0.7);
}
.contenedor-contacto {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  flex-wrap: wrap;
  padding: 1%;
  
}

/* Estilo para el título */
.titulo-contacto {
  font-size: 36px;
  text-align: center;
  width: 100%;
  margin-bottom: 50px;
  color: #fff;
}

.titulo-contacto a {
  text-decoration: none;
  color: #fff;
}


.contiene-info-mapa {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-start;
  width: 100%;
  margin-bottom: 50px;
  
}

.informacion-contacto {
  flex: 1;
  max-width: 500px;

}

.informacion-contacto ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.informacion-contacto li {
  margin-bottom: 10px;
  font-size: 18px;
  display: flex;
  align-items: center;
}

.informacion-contacto i {
  margin-right: 10px;
  color: #CE96CE;
}

#mapa {
  flex: 1;
max-width: 500px;

}

#mapa iframe {
  height: 220px;
  width: 100%;
}

@media only screen and (min-width: 768px) and (max-width: 1024px) {


.presentacion-imagenes {
  padding-left: 2%;
  padding-right: 2%;
}


.cabecera-imagen {
  height: 86px;

}

.sub-clinica {
  font-size: 2rem;

}

.parrafo-clinica {
  font-size: 1.1rem;
}

}

/* Estilos para dispositivos móviles */
@media screen and (max-width: 768px) {

  .presentacion-imagenes {
    padding-left: 1%;
    padding-right: 1%;
  }

  .presentacion-parrafo {
    max-width: 95%;
  }

/* Contenedor de las columnas */
.contenedor-clinica {
  flex-direction: column;
}

/* Columnas */
.columna-clinica {
  width: 95%;
  margin-bottom: 20px;
}

/* Imágenes de cabecera */
.cabecera-imagen {
  height: 60px;
  margin: 0 auto 10px auto;
}

/* Títulos */
.sub-clinica {
  font-size: 2rem;
}

/* Párrafos */
.parrafo-clinica {
  font-size: 1rem;
}


.contenedor-contacto {
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.contiene-info-mapa {
  flex-direction: column;
  align-items: center;
}

.informacion-contacto {
 
  margin-bottom: 10px;
  text-align: center;
}

.informacion-contacto li {
  display: block;
}

#mapa {
  margin-top: 10px;
}
  
}
</style>