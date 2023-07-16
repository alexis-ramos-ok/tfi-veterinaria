<template>
    <div class="alimentacion-page">
      <img
        class="alimentacion-page__featured-image"
        src="https://www.santalucia.es/imagenes_slw4/1574962222778/tmptmp.jpg"
        alt="ejercicio-para-mascotas"
      />
      <div class="alimentacion-page__content">
        <h1 class="alimentacion-page__title">Haces ejercicio con tu mascota?</h1>
        <p class="alimentacion-page__description">
          El ejercicio regular es importante para la salud física y mental de tu mascota. Asegúrate de proporcionarles muchas oportunidades para jugar y hacer ejercicio, como paseos, juegos y juguetes.
        </p>
        <h2 class="alimentacion-page__subtitle">Beneficios del ejercicio para tu mascota</h2>
        <p>
          El ejercicio regular proporciona una serie de beneficios para tu mascota. Ayuda a mantener un peso saludable, fortalece los músculos y las articulaciones, mejora la salud cardiovascular y promueve la agilidad. Además, el ejercicio físico también es importante para su bienestar mental, ya que ayuda a reducir el estrés, el aburrimiento y los comportamientos no deseados causados por la falta de actividad.
        </p>
        <h2 class="alimentacion-page__subtitle">Cómo incorporar el ejercicio en la rutina diaria</h2>
        <p>
          Para asegurarte de que tu mascota reciba suficiente ejercicio, incluye actividades físicas en su rutina diaria. Los paseos son una excelente manera de proporcionar ejercicio y estimulación mental. Establece un horario regular de paseos y varía las rutas para que tu mascota pueda explorar diferentes entornos. Además, juega con tu mascota utilizando juguetes interactivos, pelotas o cuerdas para fomentar el ejercicio activo y fortalecer su vínculo contigo. Considera también la posibilidad de participar en actividades como el agility o el canicross, que ofrecen un ejercicio más estructurado y divertido para tu mascota.
        </p>
        <h2 class="alimentacion-page__subtitle">Adaptar el ejercicio a las necesidades individuales</h2>
        <p>
          Es importante adaptar el nivel de ejercicio a las necesidades individuales de tu mascota. Ten en cuenta su edad, tamaño, raza y estado de salud general. Algunas razas pueden requerir más ejercicio que otras, mientras que los perros más jóvenes suelen tener más energía y necesitan actividades más intensas. Siempre observa las señales de cansancio o fatiga en tu mascota y ajusta la intensidad y duración del ejercicio en consecuencia. Consulta con tu veterinario para obtener recomendaciones específicas sobre el tipo y cantidad de ejercicio adecuado para tu mascota.
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EjercicioPage',
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