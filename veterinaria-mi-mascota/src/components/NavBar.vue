<template>
  <header>
    <section id="inicio">
      <nav :class="{ scroll: isMenuOpen }">
        <img class="logo-nav" :src="require('@/assets/veterinaria-logo.png')" alt="Logo Veterinaria" @click="toggleMenu">

        <ul class="menu" :class="{ 'menu--open': isMenuOpen }">
          <li v-if="useRouterLink"><router-link to="/">Inicio</router-link></li>
          <li v-else><a href="/">Inicio</a></li>
          <li v-if="useRouterLink"><router-link to="/ServiciosPage">Servicios</router-link></li>
          <li v-else><a href="/ServiciosPage">Servicios</a></li>
          <li v-if="useRouterLink"><router-link to="/PetShopPage">Pet Shop</router-link></li>
          <li v-else><a href="/PetShopPage">Pet Shop</a></li>
          <li v-if="useRouterLink"><router-link to="/BlogPage">Blog</router-link></li>
          <li v-else><a href="/BlogPage">Blog</a></li>
          <li v-if="useRouterLink"><router-link to="/AboutPage">About</router-link></li>
          <li v-else><a href="/AboutPage">About</a></li>
          <li v-if="useRouterLink"><router-link to="/ContactoPage">Contacto</router-link></li>
          <li v-else><a href="/ContactoPage">Contacto</a></li>
          <li v-if="username" class="user-menu" @click="isDropdownOpen = !isDropdownOpen">
            <i class="fa-solid fa-user"></i>
            <span>{{ username }}</span>
            <ul v-show="isDropdownOpen">
              <li v-if="username" class="profile-link"><a href="/perfil/">Ver perfil</a></li>
              <li><a href="#" @click="logout">Cerrar sesión</a></li>

            </ul>
          </li>

        </ul>
      </nav>
    </section>
  </header>
</template>

<script>
import ScrollMixin from '../ScrollMixin.js';

export default {
  mixins: [ScrollMixin],
  props: {
    useRouterLink: {
      type: Boolean,
      default: true
    }
  },
  data() {
  return {
    username: null,
    isDropdownOpen: false,
  };
},
methods: {
  
  getUserData() {
   
    fetch('/user-data/')
      .then(response => response.json())
      .then(data => {
        this.username = data.username;
      })
      .catch(error => {
      console.error('Error al obtener los datos del usuario:', error);
    });

  },
  logout() {
    const csrftoken = this.getCookie('csrftoken');
    fetch('/logout/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken
      }
    })
    .then(() => {
      this.username = null;
      window.location.href = '/login/';
    });
  },
  getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
},
mounted() {
  this.getUserData();
},

}
</script>

  
<style>

/* Estilos para la sección de inicio */
#inicio {
  background-color: #885ead;
  color: #fff;
}

/* Estilos para el logo de la barra de navegación */
.logo-nav {
  max-width: 80px;
  height: auto;
  margin: 5px;
}

/* Estilos para la barra de navegación */
nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;

  background-color: transparent;
  z-index: 1;
}

nav.scroll {
  background-color: #885ead;
}


/* Estilos para los elementos de la barra de navegación */
nav ul {
  display: flex;
  justify-content: center;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
  flex-grow: 1;
  text-align: center;
}

nav li {
  margin: 0 10px;
  font-size: 18px
}

nav a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.5s, box-shadow 0.5s;
}

nav a:hover {
  transition: 0.5s;
  background-color: #CE96CE;
  box-shadow: 0px 0px 10px rgba(183, 0, 255, 0.5);
}


.menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.menu li {
  margin: 0 10px;
}

.fa-user {
  margin-right: 8px;
}
.user-menu {
  position: relative;

}
.user-menu, .user-menu * {
  cursor: pointer;
}

.user-menu ul {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #885ead;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-in-out;
  z-index: 999;
  flex-direction: column;
  width: 110px;
}
.user-menu ul li {
  display: block;
  font-size: small;
  padding: 5px 0;
}

.user-menu:hover ul {
  max-height: 500px;
}
.profile-link {
  margin-top: 5px !important;
}

@media screen and (max-width: 768px) {
  nav {
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: auto;
      overflow: hidden;
      padding-bottom: 20px;
   
    }
    
    nav ul {
      flex-direction: column;
      text-align: center;
    }
    
    nav li {
      margin: 10px 0;
      font-size: 25px;
    }



    .menu {
      display: none;
    }

    .menu--open {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .user-menu ul {
    font-size: 18px;
    padding: 10px 0;
    position: static;
    width: auto;
  }

  .user-menu ul li {
    padding: 10px;
  }
    }
  </style>
  