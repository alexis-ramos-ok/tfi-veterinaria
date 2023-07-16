<template>
    <div class="alimentacion-page">
      <img
        class="alimentacion-page__featured-image"
        src="https://static.miscota.com/consejos/wp-content/uploads/2016/10/shutterstock_346619315-FILEminimizer.jpg"
        alt="cepillar_perro"
      />
      <div class="alimentacion-page__content">
        <h1 class="alimentacion-page__title">Todo sobre el cuidado de su pelaje</h1>
        <p class="alimentacion-page__description">
          Cuidar el cabello de tu mascota es importante para su salud y bienestar general. El cepillado regular puede ayudar a prevenir enredos, caída del pelo e irritación de la piel.
        </p>
        <h2 class="alimentacion-page__subtitle">Beneficios del cepillado regular</h2>
        <p>
          El cepillado regular del pelaje de tu mascota tiene múltiples beneficios. Ayuda a mantener el pelaje limpio y libre de enredos, lo que evita la formación de nudos difíciles de quitar y reduce la posibilidad de irritación de la piel. Además, el cepillado estimula la circulación sanguínea en la piel, promoviendo un pelaje más saludable y brillante. También es una excelente oportunidad para detectar parásitos externos, como pulgas o garrapatas, y tratarlos a tiempo.
        </p>
        <h2 class="alimentacion-page__subtitle">Cómo cepillar a tu mascota</h2>
        <p>
          El proceso de cepillado debe ser tranquilo y relajante tanto para ti como para tu mascota. Utiliza un cepillo adecuado para su tipo de pelaje, ya sea largo, corto, liso o rizado. Comienza cepillando suavemente desde la cabeza hacia la cola, en dirección al crecimiento del pelo. Presta especial atención a las áreas propensas a enredos, como detrás de las orejas y en el abdomen. Si encuentras algún nudo, utiliza un peine de dientes anchos o tus dedos para desenredarlo con cuidado. Recuerda premiar a tu mascota con caricias y recompensas durante y después del cepillado para hacer de esta actividad una experiencia positiva.
        </p>
        <h2 class="alimentacion-page__subtitle">Frecuencia de cepillado</h2>
        <p>
          La frecuencia de cepillado varía según la raza, el tipo de pelaje y las necesidades individuales de tu mascota. En general, se recomienda cepillar a los perros de pelo largo al menos una vez al día, mientras que los perros de pelo corto pueden necesitar un cepillado semanal o cada dos semanas. Si tu mascota tiene problemas de enredos o caída excesiva de pelo, es posible que necesite cepillado más frecuente. Consulta con tu veterinario o un peluquero canino para obtener recomendaciones específicas para tu mascota.
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PelajePage',
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