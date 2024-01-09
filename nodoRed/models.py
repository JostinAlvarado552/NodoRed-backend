from djongo import models
class Usuarios(models.Model):
    _id = models.ObjectIdField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=11)
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=20)

class Vehiculos(models.Model):
    _id = models.ObjectIdField()
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    bateria = models.IntegerField()
    estado = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

class Tarjeta(models.Model):
    _id = models.ObjectIdField()
    usuario = models.CharField(max_length=100)
    nro_tarjeta = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    fecha_caducidad = models.DateField()
    cvv = models.CharField(max_length=3)

class Renta(models.Model):
    _id = models.ObjectIdField()
    vehiculo = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    distancia = models.IntegerField()
    estado_renta = models.BooleanField()
    precio_renta = models.IntegerField()