<template>
      <div class="hero-image-a">
            <!--Imagen que cubre la parte inicial hasta barra de menús-->
                <div class="hero-text">
                  <h1>Nuestro Equipo</h1>
                </div>
        </div>

        <main>

          <section id="about">
            <div class="contiene-about">
              <h2>Nosotros</h2>
              <p>En nuestra clínica veterinaria, estamos comprometidos con brindar la mejor atención posible a tus queridos amigos peludos. Nos apasiona trabajar con animales y estamos dedicados a asegurar su salud y bienestar.</p>
              <p>Cada animal es único y merece la atención individualizada que se merece. Desde una simple revisión de rutina hasta tratamientos médicos avanzados, estamos aquí para ayudarte a cuidar de tu mascota. Ofrecemos una amplia gama de servicios, desde atención preventiva, cirugía, cuidado dental y tratamiento de emergencia.</p>
              <h3>Nuestra Misión</h3>
              <p>Nuestra misión es brindar atención veterinaria compasiva y completa a todos los animales, grandes y pequeños. Creemos que cada animal merece la mejor atención posible, y nos esforzamos por brindarla con excelencia y honestidad.</p>
              <h3>Nuestro Equipo</h3>
              <p>Nuestro equipo de veterinarios y personal de apoyo está altamente capacitado y dedicado a brindar la mejor atención posible a tus mascotas. Estamos aquí para responder cualquier pregunta que puedas tener y para asegurarnos de que tus amigos peludos reciban la atención que merecen.</p>
              <ul>
                <li>Nuestros veterinarios y técnicos están constantemente actualizando sus conocimientos y habilidades para asegurarse de que brindan el mejor cuidado posible a tus mascotas.</li>
                <li>Valoramos y respetamos a cada animal que entra por nuestras puertas y nos aseguramos de que reciban la atención personalizada que necesitan.</li>
                <li>Trabajamos en colaboración con los dueños de las mascotas para desarrollar planes de cuidado que se adapten a las necesidades específicas de cada animal.</li>
              </ul>
            </div>

          </section>
          
          

          
        </main>
</template>
<script>


export default {
  name: 'AboutPage',
  components: {

  }
}
</script>

<style>

.hero-image-a {
  position: relative;
  height: 100vh;
  background-image: url("../assets/hero-image-a.jpg");
  background-size: cover;
}

.hero-image-a::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
}

/* Estilo para el fondo de la sección */
#about {
  background-color: #ffffff; 
  padding: 80px 0; 
}

/* Estilo para el contenido de la sección */
.contiene-about {
  max-width: 1200px; 
  margin: 0 auto; /* Centra la sección en la página */
  padding: 0 20px;
}

/* Estilo para el título principal */
.contiene-about h2 {
  font-size: 36px;
  color: #542c85;
  text-align: center;
}

/* Estilo para el párrafo de introducción */
.contiene-about p:first-of-type {
  font-size: 20px; 
  color: #444444; 
  line-height: 1.5; 
  margin-bottom: 30px;
}

/* Estilo para los títulos secundarios */
.contiene-about h3 {
  font-size: 24px;
  color: #542c85;
  margin-top: 40px; 
  margin-bottom: 20px;
}

/* Estilo para los párrafos secundarios */
.contiene-about p:not(:first-of-type) {
  font-size: 18px;
  color: #666666; 
  line-height: 1.5; 
  margin-bottom: 20px; 
}

/* Estilo para la lista de viñetas */
.contiene-about ul {
  list-style: disc; /* Establece el estilo de viñetas */
  margin-left: 40px; /* Añade espacio a la izquierda de la lista */
}

/* Estilo para los elementos de la lista de viñetas */
.contiene-about li {
  font-size: 18px; 
  color: #666666; /* Color de texto gris medio */
  line-height: 1.5; 
  margin-bottom: 10px; 
}
</style>