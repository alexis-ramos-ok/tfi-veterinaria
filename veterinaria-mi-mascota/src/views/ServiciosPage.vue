<template>
     <div class="hero-image-s">
            <!--Imagen que cubre la parte inicial hasta barra de menús-->
                <div class="hero-text">
                  <h1>Nuestros Servicios</h1>
                </div>
        </div>

    <main>


        <section id="services">
            <div class="contiene-servicios">
              <h2>Servicios</h2>
              <p>
                En nuestra veterinaria pet-shop, ofrecemos una amplia gama de servicios para mantener a tus mascotas
                 saludables y felices. Desde atención preventiva hasta tratamiento de enfermedades, nuestro equipo está
                  aquí para ayudarte a cuidar de tus amigos peludos.
              </p>
              <div class="reservar">
                <button ref="reserveButton" class="btn-reservar">Reservar cita</button>
              </div>

              <div class="servicio">
                <i class="fas fa-stethoscope"></i>
                <h3>Revisión Médica</h3>
                <p>Realizamos revisiones médicas completas para detectar cualquier problema de salud temprano y prevenir enfermedades. También podemos brindarte asesoramiento sobre nutrición y cuidado general.</p>
              </div>
              <div class="servicio">
                <i class="fas fa-syringe"></i>
                <h3>Vacunación</h3>
                <p>Ofrecemos una amplia gama de vacunas para proteger a tus mascotas de enfermedades comunes. Trabajamos contigo para crear un plan de vacunación personalizado para tus mascotas.</p>
              </div>
              <div class="servicio">
                <i class="fas fa-user-md"></i>
                <h3>Cirugía</h3>
                <p>Nuestros veterinarios están altamente capacitados para realizar cirugías de rutina y de emergencia. Utilizamos tecnología de vanguardia para garantizar la seguridad y el bienestar de tus mascotas durante todo el proceso.</p>
              </div>
              <div class="servicio">
                <i class="fas fa-ambulance"></i>
                <h3>Atención de Emergencia</h3>
                <p>Estamos disponibles para atender emergencias las 24 horas del día, los 7 días de la semana. Si tu mascota necesita atención médica inmediata, llámanos y estaremos listos para ayudarte.</p>
              </div>
              <div class="servicio">
                <i class="fas fa-cut"></i>
                <h3>Peluquería</h3>
                <p>Ofrecemos servicios de peluquería profesionales para mantener a tus mascotas limpias y bien arregladas. Desde cortes de pelo hasta baños de limpieza profunda, nos aseguramos de que tus mascotas se vean y se sientan geniales.</p>
              </div>
              <div class="servicio">
                <i class="fas fa-bath"></i>
                <h3>Limpieza</h3>
                <p>Ofrecemos servicios de baño profesionales para mantener a tus mascotas limpias y saludables. Utilizamos productos de alta calidad y técnicas adecuadas para asegurar un baño seguro y cómodo para tu mascota.</p>
              </div>
              
            </div>
          </section>
          
          

    </main>

</template>

<script>
import { onMounted } from 'vue';

export default {
  name: 'ServiciosPage',
  components: {

  },
  setup() {
    onMounted(() => {
      const reserveButton = document.querySelector('.btn-reservar');
      reserveButton.addEventListener('click', () => {
        // Redirigir al usuario a la plantilla de Django para manejar la reserva de citas
        window.location.href = '/reservar-cita/';
      });
    });
  }
}
</script>

<style>
.hero-image-s {
  position: relative;
  height: 100vh;
  background-image: url("../assets/hero-s.jpg");
  background-size: cover;
  background-position: center center;
}

.hero-image-s::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* color semi-transparente */
}

/* Estilos para la sección de servicios */
#services {
  background-color: #fff;
  padding: 60px 0;
  text-align: center;
}

#services h2 {
  font-size: 36px;
  margin-bottom: 10px;
  font-weight: 700;
  color: #542c85;
}

#services p {
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 20px;
  color: #333;
  text-align: start;
  padding: 0 2%;
}

.contiene-servicios {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 50px;
}

.reservar{
  flex-basis: 100%;
  text-align: center;
  
}

.btn-reservar{
  display: block;
  margin: 0 auto;
  display: block;
  width: auto;
  padding: 10px;
  background-color: #6b3e9e;
  color: white;
  font-size: 18px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-reservar:hover{
  background-color: #5a2e8a;
}

.servicio {
  flex-basis: 300px;
}

.servicio img {
  width: 100%;
  border-radius: 5px;
  margin-bottom: 20px;
}

.servicio h3 {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 15px;
  color: #542c85;
}

.servicio p {
  font-size: 18px;
  line-height: 1.5;
  color: #333;
}

/* Estilos para los iconos de Font Awesome */
.servicio i {
  font-size: 50px;
  margin-bottom: 20px;
  color: #542c85;
}


main{
  margin: 0;
  padding: 0;
}

@media screen and (max-width: 768px) {

  .hero-text {
    font-size: 1.2rem !important;
    white-space: normal;
  }
}
</style>