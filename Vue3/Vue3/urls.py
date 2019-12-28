
from django.contrib import admin
from django.urls import path, include
from rrhh.models import Persona
from rest_framework import routers, serializers, viewsets
from rrhh.views import PersonaViewSet

#class PersonaSerializer(serializers.Serializer):
#    class Meta:
#        model = Persona
#        fields = ['nombre','edad']

#class PersonaViewSet(viewsets.ModelViewSet):
#    queryset = Persona.objects.all()
#    serializer_class = PersonaSerializer


router = routers.DefaultRouter()
router.register('personas', PersonaViewSet)











urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
