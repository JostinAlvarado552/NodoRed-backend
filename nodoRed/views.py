from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nodoRed.serializers import UserSerializer


@api_view(['POST'])
def registrar(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Usuario registrado correctamente')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)