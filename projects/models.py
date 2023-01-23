from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
solo_alfanumericos = str
solo_Digitos = int
# Funcion para validar si el usuario ingresa solo numeros
def validarNumeros(value):
    if not solo_Digitos(value):
        raise ValidationError("Solo acepta numeros")
# Funcion para validar si el usuario ingresa solo strings
def validarAlfanumericos(value):
    if not solo_alfanumericos.isalpha(value) and solo_alfanumericos.isspace(value):
        raise ValidationError("Solo acepta strings")

class Persona(models.Model):
    tipeDocument = models.CharField(max_length=2, validators=[validarAlfanumericos])
    documento = models.IntegerField(unique=True, validators=[validarNumeros])
    nombres = models.CharField(max_length=50, validators=[validarAlfanumericos])
    apellidos =models.CharField(max_length=50, validators=[validarAlfanumericos])
    email = models.EmailField(max_length=50, unique=True)
    hobbie = models.TextField(max_length=255, validators=[validarAlfanumericos])

  