<template>
     <div class="hero-image-c">
            <!--Imagen que cubre la parte inicial hasta barra de menús-->
                <div class="hero-text">
                  <h1>Contáctanos</h1>
        </div>
        </div>
        <main>
          <div class="contact-section">
            <div class="column">
              <div class="row">
                <div class="card card-dat">
                  <h3><i class="fas fa-map-marker-alt"></i> Dirección</h3>
                  <p>Av. Siempreviva 742</p>
                </div>
                <div class="card card-dat">
                  <h3><i class="fas fa-phone"></i> Teléfono</h3>
                  <p>+54 11 5555-5555</p>
                </div>
              </div>
              <div class="row">
                <div class="card card-dat">
                  <h3><i class="fas fa-clock"></i> Horarios</h3>
                  <p>Lun - Vie de 9:00 a 18:00 <br> 
                    Sábados de 9:00 a 13:00</p>
                </div>
                <div class="card card-dat">
                  <h3><i class="fa-solid fa-truck-medical"></i> Emergencias</h3>
                  <p>+54 11 5555-4444 (24/7)</p>
                </div>
              </div>
              <div class="row">
                <div class="card card-dat">
                  <h3><i class="fa-solid fa-map-location-dot"></i> Otras Sucursales</h3>
                  <p>Av. Libertad 1234, Córdoba</p>
                </div>
                <div class="card card-dat">
                  <h3><i class="fas fa-envelope"></i> Email</h3>
                  <p>info@veterinariamascotera</p>
                </div>
              </div>
            </div>
            <div class="column">
              <form class="formulario-contacto">
                <h2>Esperamos tu mensaje</h2>
                <input type="text" id="nombre" name="nombre" placeholder="Nombre" required/>
                <input type="email" id="email" name="email" placeholder="Email" required/>
                <input type="tel" id="telefono" name="telefono" placeholder="Teléfono" required/>
                <textarea id="mensaje" name="mensaje" placeholder="Escribe tu mensaje aquí" required></textarea>
                <input id="btn-contact-enviar" type="submit" value="Enviar" />
              </form>
            </div>
          </div>
          </main>
          <div class="map-container">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3400.686870335936!2d-64.1876458494149!3d-31.416289267847355!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9423a31b9d1dcf8b%3A0x4cd4a4d896e87209!2sC%C3%B3rdoba%2C%20Provincia%20de%20C%C3%B3rdoba!5e0!3m2!1sen!2sar!4v1650535245367!5m2!1sen!2sar" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
          </div>
</template>

<script>



export default {
  mounted() {
    const form = document.querySelector('.formulario-contacto');

    form.addEventListener('submit', (event) => {
      event.preventDefault();

      const nombre = document.querySelector('#nombre').value;
      const email = document.querySelector('#email').value;
      const telefono = document.querySelector('#telefono').value;
      const mensaje = document.querySelector('#mensaje').value;

      const data = {
        nombre,
        email,
        telefono,
        mensaje
      };

      const xhr = new XMLHttpRequest();
      xhr.open('POST', 'https://sheetdb.io/api/v1/coq96mpjn8rak', true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify(data));

      xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 201) {
          // Crear un elemento div para mostrar el mensaje
          const messageDiv = document.createElement("div");
          messageDiv.innerHTML = "¡Gracias por contactarnos!";
          messageDiv.style.position = "fixed";
          messageDiv.style.top = "50%";
          messageDiv.style.left = "50%";
          messageDiv.style.transform = "translate(-50%, -50%)";
          messageDiv.style.padding = "20px";
          messageDiv.style.backgroundColor = "#4CAF50";
          messageDiv.style.color = "white";

          // Agregar el elemento div al body
          document.body.appendChild(messageDiv);

          // Ocultar el mensaje después de 3 segundos
          setTimeout(function() {
            messageDiv.style.display = "none";
          }, 3000);

          document.querySelector('.formulario-contacto').reset();
        } else if (this.readyState === XMLHttpRequest.DONE && this.status !== 201) {
          // Crear un elemento div para mostrar el mensaje
          const messageDiv = document.createElement("div");
          messageDiv.innerHTML = "Error en el envío";
          messageDiv.style.position = "fixed";
          messageDiv.style.top = "50%";
          messageDiv.style.left = "50%";
          messageDiv.style.transform = "translate(-50%, -50%)";
          messageDiv.style.padding = "20px";
          messageDiv.style.backgroundColor = "#f44336";
          messageDiv.style.color = "white";

          // Agregar el elemento div al body
          document.body.appendChild(messageDiv);

          // Ocultar el mensaje después de 3 segundos
          setTimeout(function() {
            messageDiv.style.display = "none";
          }, 3000);
        }
      };
    });
  }
};

</script>

<style>
.hero-image-c {
  position: relative;
  height: 100vh;
  background-image: url("../assets/hero-c.jpg");
  background-size: cover;
}

.hero-image-c::before {
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

/*-------------- Contacto sección contacto --*/

.contact-section {
  display: flex;
  flex-wrap: wrap;
  font-family: Arial, sans-serif;
}

.column {
  flex: 1;
  margin: 10px;
}

.row {
  display: flex;
}

.card-dat {
  flex: 1;
  margin: 10px;
  padding: 20px;
  
  border-radius: 10px;
}

.card-dat:hover{
  background-color: #f0e6f6;
}

.card-dat h3 {
  margin-top: 0;
  color: #4b0082;
}

.formulario-contacto {
  margin: 10px;
  padding: 20px;
  background-color: #f0e6f6;
  border-radius: 10px;
}

.formulario-contacto h2 {
  margin-top: 0;
  color: #4b0082;
}

.formulario-contacto input[type="text"],
.formulario-contacto input[type="email"],
.formulario-contacto input[type="tel"],
.formulario-contacto textarea {
  width: 100%;
  padding: 15px;
  margin-bottom: 15px;
  box-sizing: border-box;
  
}

#btn-contact-enviar {
  background-color: #4b0082;
  color: white;
  padding: 10px 20px;
}

#btn-contact-enviar:hover {
  background-color: white;
  color: #4b0082;
  
}


.map-container {
  position: relative;
  width: 100%;
  padding-bottom: 25%;
}
.map-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

@media (max-width: 600px) {
  .column {
    flex-basis: 100%;
  }
  .row {
    flex-direction: column;
  }
  .card {
    margin-bottom: 20px;
  }
  .map-container {
    padding-bottom: 60%;
  }
}
</style>