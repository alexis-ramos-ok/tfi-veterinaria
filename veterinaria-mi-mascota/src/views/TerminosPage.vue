<template>
    <div class="contiene-ter-pol">
      <h2 class="title-ter-pol">Términos y Condiciones</h2>
  
      <p class="paragraph">Bienvenido a nuestro sitio web. Si continúa navegando y utilizando este sitio web, acepta cumplir y estar sujeto a los siguientes términos y condiciones de uso, que junto con nuestra política de privacidad rigen la relación entre usted y nuestra empresa en relación con este sitio web. Si no está de acuerdo con alguna parte de estos términos y condiciones, no utilice nuestro sitio web.</p>
  
      <p class="paragraph">El término 'nuestra empresa' o 'nosotros' o 'nos' se refiere al propietario del sitio web cuyo domicilio social es Av. Siempreviva 742. El término 'usted' se refiere al usuario o visitante de nuestro sitio web.</p>
  
      <p class="paragraph">El uso de este sitio web está sujeto a las siguientes condiciones de uso:</p>
  
      <ul class="list">
        <li class="list-item">El contenido de las páginas de este sitio web es para su información general y uso solamente. Está sujeto a cambios sin previo aviso.</li>
        <li class="list-item">Ni nosotros ni ningún tercero proporciona ninguna garantía en cuanto a la precisión, puntualidad, rendimiento, integridad o idoneidad de la información y los materiales encontrados u ofrecidos en este sitio web para cualquier propósito en particular. Usted reconoce que dicha información y materiales pueden contener imprecisiones o errores y excluimos expresamente la responsabilidad por tales imprecisiones o errores en la medida máxima permitida por la ley.</li>
        <li class="list-item">Su uso de cualquier información o material en este sitio web es enteramente bajo su propio riesgo, por lo cual no seremos responsables. Será su propia responsabilidad asegurarse de que cualquier producto, servicio o información disponible a través de este sitio web cumpla con sus requisitos específicos.</li>
        <li class="list-item">Este sitio web contiene material que es propiedad nuestra o está licenciado a nosotros. Este material incluye, pero no se limita a, el diseño, el diseño, el aspecto, la apariencia y los gráficos. La reproducción está prohibida salvo en conformidad con el aviso de derechos de autor, que forma parte de estos términos y condiciones.</li>
        <li class="list-item">Todas las marcas comerciales reproducidas en este sitio web que no son propiedad nuestra ni están licenciadas a nosotros son reconocidas en el sitio web.</li>
        <li class="list-item">El uso no autorizado de este sitio web puede dar lugar a una reclamación por daños y perjuicios y/o ser un delito penal.</li>
        <li class="list-item">De vez en cuando, este sitio web también puede incluir enlaces a otros sitios web. Estos enlaces se proporcionan para su conveniencia para proporcionar más información. No significan que respaldemos el(los) sitio(s) web(s). No tenemos ninguna responsabilidad por el contenido del(los) sitio(s) web(s) vinculado(s).</li>
        <li class="list-item">Su uso de este sitio web y cualquier disputa que surja de dicho uso del sitio web está sujeto a las leyes aplicables.</li>
      </ul>
    </div>
  </template>
  

<script>


export default {
  name: 'TerminosPage',
  components: {

  }
}
</script>

<style>
.contiene-ter-pol {
  max-width: 800px;
  margin: 90px auto 0 auto;
  padding: 40px 0;
}

.title-ter-pol {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}

.paragraph {
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 20px;
}

.list {
  list-style: none;
  margin-bottom: 20px;
}

.list-item:before {
  content: '⁕';
  color: #7440a1;
  font-weight: bold;
  display: inline-block;
  width: 1em;
  margin-left: -1em;
}

.list-item {
  font-size: 18px;
  line-height: 1.5;
}
@media (max-width: 600px) {
  .contiene-ter-pol {
    padding: 20px;
  }

  .title-ter-pol {
    font-size: 28px;
  }

  .paragraph,
  .list-item {
    font-size: 16px;
  }
}

</style>