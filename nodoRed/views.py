from bson import ObjectId
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nodoRed.models import Usuarios, Vehiculos, Renta
from nodoRed.serializers import UserSerializer, LoginSerializer, VehicleSerializer, TarjetaSerializer, RentaSerializer


@api_view(['POST'])
def registrar(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Usuario registrado correctamente')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def log(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            correo = serializer.validated_data['correo']
            contrasena = serializer.validated_data['contrasena']
            try:
                user = Usuarios.objects.get(Q(correo=correo) & Q(contrasena=contrasena))
                serializer = UserSerializer(user)
                return Response({
                    'message': 'Inicio de sesión exitoso',
                    'user_data': serializer.data
                }, status=status.HTTP_200_OK)
            except Usuarios.DoesNotExist:
                return Response({'detail': 'Credenciales incorrectas.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def getVehiculo(request):
    variable = request.data.get('vehiculo')
    vehiculos = Vehiculos.objects.filter(_id=ObjectId(variable))
    serializer = VehicleSerializer(vehiculos, many=True)
    return Response({'vehiculos':serializer.data})

@api_view(['POST'])
def getRenta(request):
    variable = request.data.get('renta')
    rentas = Renta.objects.filter(_id=ObjectId(variable))
    serializer = RentaSerializer(rentas, many=True)
    return Response({'rentas':serializer.data})

@api_view(['POST'])
def registrarVehiculo(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Vehiculo registrado correctamente')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def registrarTarjeta(request):
    serializer = TarjetaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Tarjeta registrada correctamente')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registrarRenta(request):
    serializer = RentaSerializer(data=request.data)
    if serializer.is_valid():
        renta = serializer.save()
        renta_id = str(renta._id)  # Convertimos ObjectId a cadena para la respuesta
        return Response({'mensaje': 'Renta registrada correctamente', '_id': renta_id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def estadisticas(request):
    cantidad_usuarios = Usuarios.objects.count()
    cantidad_usuarios_rol_1 = Usuarios.objects.filter(rol=1).count()
    cantidad_usuarios_rol_2 = Usuarios.objects.filter(rol=2).count()

    cantidad_vehiculos_tipo_1 = Vehiculos.objects.filter(tipo=1).count()
    cantidad_vehiculos_tipo_2 = Vehiculos.objects.filter(tipo=2).count()

    cantidad_bicicletas_estado_1 = Vehiculos.objects.filter(tipo=1,estado=1).count()
    cantidad_bicicletas_estado_2 = Vehiculos.objects.filter(tipo=1,estado=2).count()

    cantidad_scooter_estado_1 = Vehiculos.objects.filter(tipo=2, estado=1).count()
    cantidad_scooter_estado_2 = Vehiculos.objects.filter(tipo=2, estado=2).count()

    data = {
        'cantidad_usuarios': cantidad_usuarios,
        'cantidad_usuarios_rol_1': cantidad_usuarios_rol_1,
        'cantidad_usuarios_rol_2': cantidad_usuarios_rol_2,
        'cantidad_vehiculos_tipo_1': cantidad_vehiculos_tipo_1,
        'cantidad_vehiculos_tipo_2': cantidad_vehiculos_tipo_2,
        'cantidad_bicicletas_estado_1': cantidad_bicicletas_estado_1,
        'cantidad_bicicletas_estado_2': cantidad_bicicletas_estado_2,
        'cantidad_scooter_estado_1': cantidad_scooter_estado_1,
        'cantidad_scooter_estado_2': cantidad_scooter_estado_2,
    }

    return Response(data)

@api_view(['GET'])
def getVehiculos(request):
    vehiculos = Vehiculos.objects.all()
    serializer = VehicleSerializer(vehiculos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsuarios(request):
    usuarios = Usuarios.objects.all()
    serializer = UserSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def borrarUsuario(request):
    usuario_id = request.data.get('usuario_id')
    print(usuario_id)
    try:
        usuario = Usuarios.objects.get(_id=ObjectId(usuario_id))
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def borrarVehiculo(request):
    vehiculo_id = request.data.get('vehiculo_id')
    print(vehiculo_id)

    try:
        vehiculo = Vehiculos.objects.get(_id=ObjectId(vehiculo_id))
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Vehiculos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


"""@api_view(['POST'])
def actualizarUsuario(request):
    usuario_id = request.data.get('usuario_id')
    nuevoEstado = request.data.get('estado')
    nuevaBateria = request.data.get('bateria')
    try:
        usuario = Usuarios.objects.get(_id=ObjectId(usuario_id))
        vehiculo.estado = nuevoEstado
        vehiculo.bateria = nuevaBateria
        vehiculo.save()
        return Response('Usuario Actualizado Correctamente', status=status.HTTP_200_OK)
    except Vehiculos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)"""


@api_view(['POST'])
def actualizarVehiculo(request):
    vehiculo_id = request.data.get('vehiculo_id')
    nuevoEstado = request.data.get('estado')
    nuevaBateria = request.data.get('bateria')
    try:
        vehiculo = Vehiculos.objects.get(_id=ObjectId(vehiculo_id))
        vehiculo.estado = nuevoEstado
        vehiculo.bateria = nuevaBateria
        vehiculo.save()
        return Response('Vehiculo Actualizado Correctamente', status=status.HTTP_200_OK)
    except Vehiculos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def darAdministrador(request):
    usuario_id = request.data.get('usuario_id')
    nuevo_rol = request.data.get('nuevo_rol')
    print(usuario_id)
    try:
        usuario = Usuarios.objects.get(_id=ObjectId(usuario_id))
        usuario.rol = nuevo_rol
        usuario.save()
        return Response('Rol Asignado Correctamente', status=status.HTTP_200_OK)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def actualizarUsuario(request):
    usuario_id = request.data.get('usuario_id')
    nuevaEdad = request.data.get('edad')
    nuevoTelefono = request.data.get('telefono')
    nuevoCorreo = request.data.get('correo')
    nuevaClave = request.data.get('contrasena')
    try:
        usuario = Usuarios.objects.get(_id=ObjectId(usuario_id))
        usuario.edad = nuevaEdad
        usuario.telefono = nuevoTelefono
        usuario.correo = nuevoCorreo
        usuario.contrasena = nuevaClave
        usuario.save()
        return Response('Usuario Actualizado Correctamente', status=status.HTTP_200_OK)
    except Vehiculos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


