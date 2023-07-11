<template>
     <div class="hero-image blog">
      <!--Imagen que cubre la parte inicial hasta barra de menús-->
      <div class="hero-text">
        <h1>Recomendaciones y Consejos</h1>
      </div>
    </div>

    <main>
      <section class="blog" id="presentacion">
        <div class="contenedor-presentacion" id="cont-blog">
          <h2>Buscador</h2>
        </div>
  <div id="search-box">
    <form id="search-form" @submit.prevent="search">
      <input id="search-text" type="text" v-model="query" placeholder="Busca un blog" aria-label="Buscar un blog" />
      <button id ="search-button" type="submit">Busca!</button>
    </form>
  </div>
  <div id="search-results">
    <div v-for="result in results" :key="result.link" class="result-container">
      <img :src="result.link" :alt="result.title" class="result-image" />
      <h3 class="result-title"><a :href="result.link">{{ result.title }}</a></h3>
      <p class="result-snippet">{{ result.snippet }}</p>
    </div>
  </div>
    <div class="blog-cajas">

      <article class="container-card card-1">
  <div class="img-card">
    <img
      src="https://static.miscota.com/consejos/wp-content/uploads/2016/10/shutterstock_346619315-FILEminimizer.jpg"
      alt="cepillar_perro"
    />
  </div>
  <div class="text-card">
    <h3>Todo sobre el cuidado de su pelaje</h3>
    <p class="fecha">18/05/23</p>
    <div>
      <p>
        Cuidar el cabello de tu mascota es importante para su salud y bienestar general. El cepillado regular puede ayudar a prevenir enredos, caída del pelo e irritación de la piel.
      </p>
    </div>
  </div>
</article>

<article class="container-card card-2">
  <div class="img-card">
    <img
      src="https://www.eluniverso.com/resizer/bK8SrLrW9M4jehIdkdCcRLMPaoM=/813x670/smart/filters:quality(70)/cloudfront-us-east-1.images.arcpublishing.com/eluniverso/HNPPMBADKNEYBLUO37M6NLHSCM.jpg"
      alt="alimento-para-animales"
    />
  </div>
  <div class="text-card">
    <h3>Claves en su alimentación</h3>
    <p class="fecha">28/05/23</p>
    <div>
      <p>
        Alimentar a tu mascota con una dieta equilibrada y nutritiva es esencial para su salud. Consulta con tu veterinario para determinar el mejor alimento para tu mascota según su edad, raza y necesidades de salud.
      </p>
    </div>
  </div>
</article>

<article class="container-card card-3">
  <div class="img-card">
    <img
      src="https://www.santalucia.es/imagenes_slw4/1574962222778/tmptmp.jpg"
      alt="ejercicio-para-mascotas"
    />
  </div>
  <div class="text-card">
    <h3>Haces ejercicio con tu mascota?</h3>
    <p class="fecha">07/06/23</p>
    <div>
      <p>
        El ejercicio regular es importante para la salud física y mental de tu mascota. Asegúrate de proporcionarles muchas oportunidades para jugar y hacer ejercicio, como paseos, juegos y juguetes.
      </p>
    </div>
  </div>
</article>
<article class="container-card card-4">
  <div class="img-card">
    <img
      src="https://www.mundoperro.net/wp-content/uploads/convivencia-perros-gatos-1200x741.jpg"
      alt="socializacion-de-mascotas"
    />
  </div>
  <div class="text-card">
    <h3>Socialización y Mascotas</h3>
    <p class="fecha">17/06/23</p>
    <div>
      <p>
        La socialización es importante para el desarrollo y bienestar de tu mascota. Exponlos a una variedad de personas, animales y entornos para ayudarlos a ser bien adaptados y seguros.
      </p>
    </div>
  </div>
</article> 

        </div>
      </section>
    </main>
</template>

<script>
export default {
  data() {
    return {
      query: '',
      results: []
    }
  },
  methods: {
  search() {
    const cx = '66881dcc9643d48a2';
    const apiKey = 'AIzaSyCytzYEgeJIJqjnm0qbef3fBql0CIXtMfI';
    const query = `${this.query} blog mascotas`;
    const url = `https://www.googleapis.com/customsearch/v1?key=${apiKey}&cx=${cx}&q=${query}&lr=lang_es&searchType=image`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        this.results = data.items;
      });
  }
}

}
</script>

<style>
/*----------------BUSCADOR*/

.hero-image.blog {
  position: relative;
  height: 100vh;
  background-image: url("../assets/blog.png");
  background-size: cover;
}

.hero-image.blog::before {
 
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

.blog {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.contenedor-presentacion {
  color: #6c3483; /* texto en morado */
}

#search-box {
  display: flex;
  justify-content: center;
  margin-bottom: 2%;
}

#search-form {
  display: flex;
  margin-bottom: 10px;
}

#search-text {
  flex: 1;
  padding: 10px;
  border: none;
  border-bottom: 2px solid #ddd;
  color: #6c3483; /* texto en morado */
}

#search-button {
  margin-left: 10px;
  padding: 10px;
  background-color: #6c3483; /* fondo en morado */
  color: #fff; /* texto en blanco */
  border: none;
  cursor: pointer;
  transition: all 0.3s ease-in-out; /* efecto de transición suave */
}

#search-button:hover {
  background-color: #fff; /* fondo en blanco */
  color: #6c3483; /* texto en morado */
  border: 1px solid #6c3483; /* borde en morado */
}

.blog-cajas {
  display: flex;
  flex-wrap: wrap;
}

.container-card {
  background-color:#fff;
  border-radius:.5rem;
  box-shadow :0 .5rem .5rem rgba(0,0,0,.2);
  padding :20px;
  width:min(250px,100%);
  margin:auto;
  margin-bottom :20px;

}

.container-card:hover {
    transform : scale(1.01);
    box-shadow :0px .5rem .5rem rgba(0,0,0,.2);
}


.img-card img {
  width: 250px;
  height: 250px;
  display: block;
  margin: 0 auto;
  object-fit: cover;

}

.text-card h3{
  font-size :22px;
  font-weight:bold;
  margin-top: 5px;
  margin-bottom: 0;
  color:#8b42a8;

}

.text-card p{
  font-size :16px;
  line-height :1.5;
  margin-top: 0;
  margin-bottom: 0;
  color:#333;

}

.fecha{
  font-size :14px;
  color:#888;
  justify-self:end;
  margin: 0 auto;
}

#search-results{
  display:flex;
  flex-wrap :wrap;

}

.result-container{
    
  background-color:#fff;
  border-radius:.5rem;
  box-shadow :0 .5rem .5rem rgba(0,0,0,.2);
  padding :20px;
  width:min(250px,100%);
  margin:auto;
  margin-bottom :20px;

}
.result-image {
  width: 250px;
  height: 250px;
  display: block;
  margin: 0 auto;
  object-fit: cover;
}

.result-title{
    
  margin :0;
  font-size :18px;
  font-weight:bold;

}

.result-snippet{

  margin :0;
  font-size :14px;
  color:#666;

}


@media only screen and (max-width:768px){
    
.hero-image.blog{ 
  background-image:url("../assets/blog-m.png");

}

.blog .hero-text{
    
  font-size: 0.8rem !important;

}

}

@media (max-width :600px){

#search-results{

  grid-template-columns :repeat(auto-fit,minmax(100%,1fr));

}
.result-container, .container-card {
    width: 100%;
    padding: 10px;
  }
  .result-image, .img-card img {
    width: 100%;
    height: auto;
  }
  .result-title, .text-card h3 {
    text-align: center;
    font-size: 20px;
  }
  .result-snippet, .text-card p {
    font-size: 15px;
  }
}

</style>