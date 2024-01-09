from rest_framework import serializers

from nodoRed.models import Usuarios


class UserSerializer(serializers.Serializer):
    class Meta:
        model = Usuarios
        fields = '__all__'