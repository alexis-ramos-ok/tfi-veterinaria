<template>
    <div class="alimentacion-page">
      <img
        class="alimentacion-page__featured-image"
        src="https://www.eluniverso.com/resizer/bK8SrLrW9M4jehIdkdCcRLMPaoM=/813x670/smart/filters:quality(70)/cloudfront-us-east-1.images.arcpublishing.com/eluniverso/HNPPMBADKNEYBLUO37M6NLHSCM.jpg"
        alt="alimento-para-animales"
      />
      <div class="alimentacion-page__content">
  <h1 class="alimentacion-page__title">Claves en la alimentación de tu mascota</h1>
  <p class="alimentacion-page__description">
    Alimentar a tu mascota con una dieta equilibrada y nutritiva es esencial para su salud y bienestar. Una dieta adecuada puede ayudar a prevenir enfermedades, mantener un peso saludable y mejorar la calidad de vida de tu mascota.
  </p>
  <h2 class="alimentacion-page__subtitle">Consulta con tu veterinario</h2>
  <p>
    Es importante consultar con tu veterinario para determinar el mejor alimento para tu mascota según su edad, raza y necesidades de salud. Tu veterinario tiene el conocimiento necesario para evaluar las necesidades nutricionales específicas de tu mascota y puede recomendarte un alimento que se ajuste a ellas. Además, también te proporcionará información sobre la cantidad adecuada de alimento que debes darle a tu mascota, teniendo en cuenta su tamaño, nivel de actividad y otros factores relevantes.
  </p>
  <h2 class="alimentacion-page__subtitle">Elige alimentos de alta calidad</h2>
  <p>
    Al elegir alimentos para tu mascota, opta por opciones de alta calidad que contengan ingredientes nutritivos y sean adecuados para su edad y estilo de vida. Busca alimentos que sean formulados específicamente para su etapa de vida (cachorro, adulto, senior) y considera sus necesidades específicas, como el tamaño de la raza y posibles condiciones de salud. Evita los alimentos que contengan subproductos, rellenos y conservantes artificiales, ya que estos pueden tener un impacto negativo en la salud de tu mascota a largo plazo.
  </p>
  <h2 class="alimentacion-page__subtitle">Proporciona agua fresca</h2>
  <p>
    Junto con una alimentación adecuada, es fundamental proporcionarle a tu mascota agua fresca en todo momento. El agua es esencial para mantenerla hidratada y ayudar en el funcionamiento óptimo de sus sistemas corporales. Asegúrate de que el recipiente de agua esté siempre limpio y lleno, y cámbialo regularmente para mantener su frescura. Siempre ten en cuenta la cantidad de agua que tu mascota necesita, ya que puede variar según su tamaño, actividad y las condiciones ambientales.
  </p>
</div>

    </div>
  </template>
  
  <script>
  export default {
    name: 'AlimentacionPage',
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
  