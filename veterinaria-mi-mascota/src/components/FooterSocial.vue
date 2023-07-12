<template>
          <!--Footer derechos y desarrollador-->
          <footer>
        <div class="footer-title-container">
          <hr />
          <h2 class="footer-title">Mi Mascota</h2>
          <hr />
        </div>
        <div class="footer-links">
          <a class="politica" href="/PoliticaPage">Política de privacidad</a>
          <div class="contenedor-redes-sociales">
            <div class="redes-sociales">
              <a href="#"><i class="fab fa-facebook-f"></i></a>
              <a href="#"><i class="fab fa-twitter"></i></a>
              <a href="#"><i class="fab fa-instagram"></i></a>
              <a href="#"><i class="fa-brands fa-whatsapp"></i></a>
              <a href="#"><i class="fa-brands fa-telegram"></i></a>
            </div>
          </div>
          <a class="terminos" href="/TerminosPage">Términos y condiciones</a>
        </div>
        <h3 class="titulo-novedades">Novedades semanales</h3>
        <form action="" class="subscribe-form">
          <input type="email" placeholder="Email" />
          <button type="submit">Suscribirse</button>
        </form>
        <p>© 2023 Mi Mascota Veterinaria. Todos los derechos reservados. Desarrollado por Alexis Ramos ✨</p>
      </footer>
      
</template>

<script>
export default {
  // Component options
}
</script>

<style>
.contenedor-redes-sociales {

text-align: center;
}

.redes-sociales {
display: inline-block;
}

.redes-sociales a {
display: inline-block;
margin: 0 20px;
font-size: 30px;
color: #CE96CE;
transition: all 0.3s ease-in-out;
}

.redes-sociales a:hover {
transform: scale(1.2);
color: #fff;
}



.redes-sociales a i {
transition: all 0.3s ease-in-out;
}

.redes-sociales a:hover i {
transform: rotate(360deg);
transition: all 0.3s ease-in-out;
}





/* Estilos para el pie de página */
footer {
background-color: #885ead;
color: #fff;
text-align: center;
padding: 10px 0;
}

footer p {
margin: 0;
padding: 0;
font-family: Arial, Helvetica, sans-serif;
font-size: small;
}



.titulo-novedades{
margin-bottom: 0;
margin-top: 25px;
}

.footer-title-container {
display: flex;
align-items: center;
}

.footer-title-container hr {
width: 30%;
}

.footer-links {
display: flex;
justify-content: space-around;
align-items: center;
padding: 10px 0;
}



.subscribe-form {
display: flex;
justify-content: center;
align-items: center;
max-width: 400px;
margin: 0 auto;
padding: 20px 2% 30px 2%;
background-color: #885ead;

}

.subscribe-form input {
flex: 1;
margin-right: 0;
height: 30px;
border: solid #fff;
background-color: #885ead;
border-right: none;
}

.subscribe-form button {
border: solid #fff;
height: 38px;
background-color: #885ead;
color:#fff
}

.subscribe-form input:focus,
.subscribe-form button:hover {
background-color: #d9b3ff;
}

.terminos, .politica{
color: #CE96CE;
text-decoration: none;
transition: all 0.3s ease-in-out
}

.terminos:hover, .politica:hover{
color: #fff
}

@media screen and (max-width: 768px) {
.redes-sociales {
  margin-top: 15px;
  margin-bottom: 15px;
}
    
.redes-sociales a {
  margin: 0 10px;
  width: 40px;
  height: 40px;
  line-height: 40px;
  font-size: 20px;
  }
        
.redes-sociales a i {
  font-size: 30px;
}
}

@media (max-width: 600px) {
  .footer-links {
    display: flex;
    flex-wrap: wrap;
  }
  .contenedor-redes-sociales {
    order: -1;
    width: 100%;
  }
  .politica, .terminos {
    font-size: 14px;
    text-align: center;
    width: 50%;
  }
   
  .subscribe-form input{
    width:auto;
   }
   
  .subscribe-form button{
    margin-right:auto;
    margin-left:auto; 
   }
  }
</style>