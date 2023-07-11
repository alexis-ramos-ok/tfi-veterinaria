<template>
<div class="hero-image-p">
    <!--Imagen que cubre la parte inicial hasta barra de menús-->
        <div class="hero-text">
          <h1></h1>
        </div>
</div>

<main>
<section id="petshop">
    <h2 class="section-title">Artículos</h2>
    <div class="petshop-container">
      <div class="product-card">
        <img src="../assets/articulo1.webp" alt="Comida para gato">
        <h3 class="product-title">Comida para cobayo</h3>
        <p class="product-price">$10.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
      <div class="product-card">
        <img src="../assets/articulo3.png" alt="Comida para perro">
        <h3 class="product-title">Comida para gato</h3>
        <p class="product-price">$12.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
      <div class="product-card">
        <img src="../assets/articulo4.png" alt="Juguete para gato">
        <h3 class="product-title">Juguete para gato</h3>
        <p class="product-price">$5.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
      <div class="product-card">
        <img src="../assets/articulo5.webp" alt="Comida para perro">
        <h3 class="product-title">Comida para perro</h3>
        <p class="product-price">$7.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>

      <div class="product-card">
        <img src="../assets/articulo6.jpg" alt="Árbol para gato">
        <h3 class="product-title">Árbol para gato</h3>
        <p class="product-price">$10.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
      <div class="product-card">
        <img src="../assets/articulo7.jpg" alt="Comida para perro">
        <h3 class="product-title">Cama colgante gato</h3>
        <p class="product-price">$12.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
      <div class="product-card">
        <img src="../assets/articulo8.png" alt="Juguete para gato">
        <h3 class="product-title">Litera</h3>
        <p class="product-price">$5.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
      <div class="product-card">
        <img src="../assets/articulo9.jpg" alt="Juguete para perro">
        <h3 class="product-title">Baño gato</h3>
        <p class="product-price">$7.00</p>
        <button class="btn-add-to-cart">Agregar al carrito</button>
      </div>
    </div>
    <div class="cart-container">
      <h3 class="cart-title">Carrito de compras</h3>
      <ul class="cart-items">
        <!-- los items agregados al carrito serán insertados aquí con JavaScript -->
      </ul>
      <p class="cart-total">Total: <span id="cart-total">$0.00</span></p>
      <button class="btn-checkout" @click="proceedToPayment">Proceder al pago</button>
    </div>
  </section>
  
</main>

<div id="modal-container">
<div id="modal">
  <button id="modal-close-btn" @click="closePaymentModal">&times;</button>
  <h2>Total a pagar: <span id="modal-total"></span></h2>
  <form id="payment-form">
    <label for="card-number">Número de tarjeta:</label>
    <input type="text" id="card-number" required>
    <label for="card-expiry">Fecha de expiración:</label>
    <input type="text" id="card-expiry" placeholder="MM/AA" required>
    <label for="card-cvc">CVC:</label>
    <input type="text" id="card-cvc" required>
    <button type="submit" @click="processPayment">Pagar</button>
  </form>
</div>
</div>
<div class="notification"></div>
</template>

<script>
import { onMounted, reactive, toRefs, watch } from 'vue';

export default {
  setup() {
    const state = reactive({
      cartItems: {},
      cartTotal: 0,
      showNotification: false
    });
    watch(
      () => state.showNotification,
      (newValue) => {
        const notificationDiv = document.querySelector('.notification');
        notificationDiv.textContent = 'Agregado al carrito';
        if (newValue) {
          notificationDiv.classList.add('show');
        } else {
          notificationDiv.classList.remove('show');
        }
      }
    );


    const updateCart = () => {
      state.cartTotal = 0;
      const cartItemsContainer = document.querySelector('.cart-items');
      cartItemsContainer.innerHTML = '';
      const table = document.createElement('table');
      const thead = document.createElement('thead');
      const tr = document.createElement('tr');
      const th1 = document.createElement('th');
      const th2 = document.createElement('th');
      const th3 = document.createElement('th');
      th1.textContent = 'Artículo';
      th2.textContent = 'Cantidad';
      th3.textContent = '$ x Ud';
      tr.appendChild(th1);
      tr.appendChild(th2);
      tr.appendChild(th3);
      thead.appendChild(tr);
      table.appendChild(thead);
      const tbody = document.createElement('tbody');
      for (const [title, item] of Object.entries(state.cartItems)) {
        state.cartTotal += item.price * item.quantity;
        const tr = document.createElement('tr');
        const td1 = document.createElement('td');
        const td2 = document.createElement('td');
        const td3 = document.createElement('td');
        td1.textContent = title;
        td2.innerHTML = `
          <div>
            <button class="btn-decrease-quantity">-</button>
            <span class="quantity">${item.quantity}</span>
            <button class="btn-increase-quantity">+</button>
            <button class="btn-remove-item">x</button>
          </div>
        `;
        td3.textContent = `$${item.price.toFixed(2)}`;
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tbody.appendChild(tr);
      }
      table.appendChild(tbody);
      cartItemsContainer.appendChild(table);
            // actualizar el total del carrito
            const cartTotalElement = document.querySelector('#cart-total');
      cartTotalElement.textContent = `$${state.cartTotal.toFixed(2)}`;
    };

    onMounted(() => {
      const addToCartBtns = document.querySelectorAll('.btn-add-to-cart');

      
      addToCartBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const product = btn.parentElement;
          const title = product.querySelector('.product-title').textContent;
          const price = parseFloat(product.querySelector('.product-price').textContent.replace('$', ''));

          if (title in state.cartItems) {
            state.cartItems[title].quantity++;
          } else {
            state.cartItems[title] = { price, quantity: 1 };
          }

          updateCart();
          state.showNotification = true;
          setTimeout(() => {
            state.showNotification = false;
          }, 2000);
          
        });
      });

      document.addEventListener('click', event => {
        if (event.target.classList.contains('btn-remove-item')) {
          const productTitle = event.target.parentElement.parentElement.parentElement.querySelector('td:first-child').textContent;
          delete state.cartItems[productTitle];
          updateCart();
        } else if (event.target.classList.contains('btn-increase-quantity')) {
          const productTitle = event.target.closest('tr').querySelector('td:first-child').textContent;
          state.cartItems[productTitle].quantity++;
          updateCart();
        } else if (event.target.classList.contains('btn-decrease-quantity')) {
          const productTitle = event.target.closest('tr').querySelector('td:first-child').textContent;
          if (state.cartItems[productTitle].quantity > 1) {
            state.cartItems[productTitle].quantity--;
          } else {
            delete state.cartItems[productTitle];
          }
          updateCart();
        }
      });
    });

    return {
  ...toRefs(state),
  updateCart,
  proceedToPayment() {
    const modalContainer = document.querySelector('#modal-container');
    const modalTotal = document.querySelector('#modal-total');
    modalTotal.textContent = `$${state.cartTotal.toFixed(2)}`;
    modalContainer.style.display = 'block';
  },
  closePaymentModal() {
    const modalContainer = document.querySelector('#modal-container');
    modalContainer.style.display = 'none';
  },
  processPayment() {
    const paymentForm = document.querySelector('#payment-form');
    paymentForm.addEventListener('submit', event => {
      event.preventDefault();
      this.closePaymentModal();
      alert('Pago procesado correctamente');
    });
  }
};



  }
};

</script>

<style>

.hero-image-p {
  position: relative;
  height: 100vh;
  background-image: url("../assets/pet-shop.png");
  background-size: cover;
  background-position: center center;
}

.hero-image-p::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3); /* color semi-transparente */
}

#petshop {
  background-color: white;
  padding: 50px 0 0 0;
}

.section-title {
  text-align: center;
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 30px;
  color: #6b3e9e;
}

.petshop-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
}

.product-card {
  width: 300px;
  background-color: #f7f7f7;
  border: 1px solid #ebebeb;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: box-shadow 0.3s ease;
}

.product-card:hover {
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
}

.product-card img {
  display: block;
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-title {
  font-size: 24px;
  font-weight: bold;
  margin: 20px 0 10px;
  color: #6b3e9e;
}

.product-price {
  font-size: 18px;
  font-weight: bold;
  margin: 0 0 20px;
  color: #6b3e9e;
}

.btn-add-to-cart {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #6b3e9e;
  color: white;
  font-size: 18px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-add-to-cart:hover {
  background-color: #5a2e8a;
}


.cart-container {
  background-color: #6b3e9e;
  color: white;
  padding: 30px;
  margin-top: 30px;
}

.cart-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.cart-items {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}



/* Agregar una clase a la tabla */
.table-cart {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

/* Estilos para las celdas de encabezado */
.table-cart th {
  background-color: #f2f2f2;
  text-align: left;
  padding: 8px;
  font-size: 18px;
}

/* Estilos para las celdas de cuerpo */
.table-cart td {
  border-bottom: 1px solid #ddd;
  padding: 8px;
  font-size: 16px;
}

/* Estilos para los botones de cantidad */
.btn-decrease-quantity,
.btn-increase-quantity {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 8px;
  font-size: 16px;
  cursor: pointer;
}

.btn-remove-item {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 8px;
  font-size: 16px;
  cursor: pointer;
}

.btn-remove-item:hover{
  background-color: #cf2a1e;
}

.btn-decrease-quantity:hover,
.btn-increase-quantity:hover
 {
  background-color: #3e8e41;
}
.quantity {
  font-size: 1.1rem;
  margin: 0 0.4rem;
}

.notification {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
  z-index: 9999;
}


.notification.show {
  opacity: 1;
}


@media screen and (max-width: 600px) {
  .table-cart {
    width: 100%;
  }

  .table-cart thead {
    display: none;
  }

  .table-cart tbody tr {
    display: block;
    margin-bottom: 10px;
    border-bottom: 1px solid #ddd;
  }

  .table-cart tbody td:before {
    content: attr(data-label);
    float: left;
    font-weight: bold;
    text-transform: uppercase;
  }
 
}

@media only screen and (max-width: 768px) {
  td > div {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .btn-remove-item {
    margin-left: 10px;
  }
  .hero-image-p{
    background-image: url("../assets/pet-shop-m.png");
  }

}




.cart-item-title {
  font-size: 18px;
  font-weight: bold;
}

.cart-item-price {
  font-size: 18px;
}

.cart-total {
  font-size: 24px;
  font-weight: bold;
  margin: 20px 0;
}

.btn-checkout {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #5a2e8a;
  color: white;
  font-size: 18px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-checkout:hover {
  background-color: #4c2678;
}


#modal-container {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

#modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

#modal h2 {
  margin-top: 0;
}

#payment-form label {
  display: block;
  margin-bottom: 5px;
}

#payment-form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  box-sizing: border-box;
}

#payment-form button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

#modal-close-btn {
  position: absolute;
  top: 3px;
  right: 10px;
  font-size: 24px;
  background-color: transparent;
  border: none;
  cursor: pointer;
}

#modal-close-btn:hover {
  color: red;
}
@media screen and (max-width: 480px) {
  #modal {
    width: 90%;
    padding: 10px;
  }

  #payment-form input {
    font-size: 16px;
    padding: 5px;
  }

  #modal-close-btn {
    font-size: 16px;
  }
}
</style>