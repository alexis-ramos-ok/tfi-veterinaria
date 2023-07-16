<template>
    <div class="alimentacion-page">
      <img
        class="alimentacion-page__featured-image"
        src="https://www.mundoperro.net/wp-content/uploads/convivencia-perros-gatos-1200x741.jpg"
        alt="socializacion-de-mascotas"
      />
      <div class="alimentacion-page__content">
        <h1 class="alimentacion-page__title">Socialización y Mascotas</h1>
        <p class="alimentacion-page__description">
          La socialización es importante para el desarrollo y bienestar de tu mascota. Exponerlos a una variedad de personas, animales y entornos les ayuda a ser bien adaptados y seguros.
        </p>
        <h2 class="alimentacion-page__subtitle">Beneficios de la socialización</h2>
        <p>
          La socialización temprana y continua es esencial para tu mascota. Les ayuda a desarrollar habilidades de comunicación, a sentirse cómodos en diferentes situaciones y a prevenir comportamientos no deseados. La socialización adecuada promueve la confianza, la sociabilidad y la capacidad de adaptación de tu mascota, lo que les permite tener interacciones positivas con otros animales, personas y su entorno en general.
        </p>
        <h2 class="alimentacion-page__subtitle">Cómo socializar a tu mascota</h2>
        <p>
          Comienza la socialización de tu mascota desde una edad temprana. Presenta gradualmente diferentes estímulos, como personas amigables, otros animales y diferentes entornos. Asegúrate de que las interacciones sean positivas y seguras, utilizando refuerzos positivos, elogios y recompensas. Haz que las experiencias sean gradualmente más desafiantes a medida que tu mascota se sienta cómoda. Participar en clases de socialización y obediencia también puede ser beneficioso para tu mascota, brindándoles la oportunidad de interactuar con otros perros y recibir instrucción profesional.
        </p>
        <h2 class="alimentacion-page__subtitle">Continuar la socialización a lo largo de la vida</h2>
        <p>
          La socialización no debe detenerse en la etapa de cachorro. Continúa exponiendo a tu mascota a nuevas personas, animales y entornos a medida que crece. Participa en actividades de socialización, como visitas al parque para perros, paseos en áreas concurridas y encuentros controlados con otros animales. Recuerda siempre estar atento a las señales de estrés o incomodidad de tu mascota y ajustar el nivel de socialización según sus necesidades individuales.
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SocializacionPage',
  }
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
  .alimentacion-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.alimentacion-page__featured-image {
  height: auto;
  max-height: 80vh;
  object-fit: cover;
}

.alimentacion-page__content {
  width: 100%;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
}

.alimentacion-page {
  font-family: 'Open Sans', sans-serif;
}

.alimentacion-page__title {
  font-size: 34px;
  margin-bottom: 10px;
  color: #7c18be;
  text-align: center;
}

.alimentacion-page__subtitle {
  font-size: 24px;
  margin-top: 20px;
  margin-bottom: 10px;
  color: #7c18be;
}

.alimentacion-page__description {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 20px;
  color: #555;
}

@media (min-width: 768px) {
   
    .alimentacion-page__subtitle,
    .alimentacion-page__description {
        text-align:left
    }
}
@media (min-width: 768px) {
   
   .alimentacion-page__subtitle,
   .alimentacion-page__description {
       text-align:left
   }
}
@media (max-width:900px) {
   
   .alimentacion-page__title,
   .alimentacion-page__subtitle,
   .alimentacion-page__description {
       text-align:center
   }
   .alimentacion-page__featured-image {
 width: 100%;
 }

}
  </style>