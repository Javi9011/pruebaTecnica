from .models import Persona
from rest_framework import viewsets, permissions
from .serializers import PersonaSerializers
from rest_framework.response import Response
from rest_framework import status

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializers
#Validaciones
    def user_api_view(request):
    #Metodo listar
     if request.method == 'GET':
        users = Persona.objects.all()
        users_serializer = PersonaSerializers(users,many =True)

        test_data = {
            request
        }
        test_user = PersonaSerializers(data = test_data)
        if test_user.is_valid():
            print("Validaciones correctas")
        else:
            print(test_user.errors)

        return Response(users_serializer.data,status = status.HTTP_200_OK)
#Metodo crear
     elif request.method == 'POST':
        user_serializer = PersonaSerializers(data =  request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Persona creada correctamente'},status = status.HTTP_201_CREATED)

        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


