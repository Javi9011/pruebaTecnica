from .models import Persona
from rest_framework import viewsets, permissions
from .serializers import PersonaSerializers
from rest_framework.response import Response
from rest_framework import status

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializers



