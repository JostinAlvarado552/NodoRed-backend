from rest_framework import serializers

from nodoRed.models import Usuarios, Vehiculos, Tarjeta, Renta


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    correo = serializers.CharField()
    contrasena = serializers.CharField()


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'

class RentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renta
        fields = '__all__'

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'
