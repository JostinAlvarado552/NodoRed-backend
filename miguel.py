import os
from datetime import datetime

import django
from django.utils import timezone
from bson import ObjectId  # Asegúrate de importar ObjectId de la biblioteca bson

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nodoRed.settings")
django.setup()

# Importar modelos de Django
from nodoRed.models import Tarjeta, Usuarios, Vehiculos, Renta

# Insertar datos en la tabla Usuarios
usuario = Usuarios.objects.create(
    nombres='Juan',
    apellidos='Pérez',
    edad=30,
    telefono=987654321,
    correo='juan.perez@example.com',
    contrasena='contraseñasegura'
)

# Insertar datos en la tabla Vehiculos con tipo 'bicicleta'
vehiculo = Vehiculos.objects.create(
    tipo='bicicleta',
    modelo='Bicicleta Eléctrica',
    marca='MarcaBici',
    bateria=70,
    estado='Disponible',
    latitude='37.7749',
    longitude='-122.4194'
)



# Insertar datos en la tabla Tarjeta
tarjeta = Tarjeta.objects.create(
    nro_tarjeta='1234567890123456',
    nombre='Juan Pérez',
    fecha_caducidad='2024-12-31',
    cvv='123'
)

# Insertar datos en la tabla Renta
renta = Renta.objects.create(
    _idVehiculo=vehiculo._idVehiculo,
    _idUsuario=usuario._idUsuario,
    fecha_inicio=datetime(2024, 1, 9, 10, 0, 0),
    fecha_fin=datetime(2024, 1, 9, 12, 0, 0),
    distancia=50,
    estado_renta=True,
    precio_renta=75.0
)
