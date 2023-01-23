from rest_framework import serializers
from .models import Persona


class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','tipeDocument','documento','nombres','apellidos','email','hobbie')


        
    

       