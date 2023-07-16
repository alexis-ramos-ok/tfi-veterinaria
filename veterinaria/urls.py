from django.contrib import admin
from django.urls import path
from veterinariaMiMascota import views
from django.contrib.auth import views as auth_views
from veterinariaMiMascota.views import user_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_view, name='my_view'),
    path('reservar-cita/', views.reservar_cita, name='reservar_cita'),
    path('lista-de-horas/<int:dia>/', views.lista_de_horas, name='lista_de_horas'),
    path('crear/<int:dia>/<str:hora>/', views.crear_cita, name='crear_cita'),

    path('ServiciosPage/', views.servicios_page, name='servicios_page'),
    path('PetShopPage/', views.pet_shop_page, name='pet_shop_page'),
    path('BlogPage/', views.blog_page, name='blog_page'),
    path('AboutPage/', views.about_page, name='about_page'),
    path('ContactoPage/', views.contacto_page, name='contacto_page'),
    path('login/', views.login_or_register_view, name='login'),
    path('user-data/', user_data, name='user-data'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('eliminar/<int:dia>/<str:hora>/', views.eliminar_cita, name='eliminar_cita'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('PoliticaPage/', views.politica_page, name='politica_page'),
    path('TerminosPage/', views.terminos_page, name='terminos_page'),
    path('PelajePage/', views.terminos_page, name='pelaje_page'),
    path('AlimentacionPage/', views.terminos_page, name='alimentacion_page'),
    path('EjercicioPage/', views.terminos_page, name='ejercicios_page'),
    path('SocializacionPage/', views.terminos_page, name='socializacion_page'),
]
