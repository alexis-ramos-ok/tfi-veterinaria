from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pet_name = models.CharField(max_length=30)
    pet_breed = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Cita(models.Model):
    dia = models.IntegerField()
    hora = models.TimeField()
    hora_texto = models.CharField(max_length=5)
    nombre_mascota = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    nombre_dueno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
