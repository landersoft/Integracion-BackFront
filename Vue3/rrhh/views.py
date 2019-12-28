from django.shortcuts import render
from .models import Persona
from rest_framework import viewsets
from rrhh.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


def index(request):
    return render(request, 'index.html')



