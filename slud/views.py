from slud.serializers import SpeakerSerializer, CharlaSerializer, SponsorSerializer
from rest_framework import viewsets #conjunto de vistas
from slud.models import Speaker, Charla, Sponsor
from rest_framework import permissions
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect('/api/')

class SpeakerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Speaker.objects.order_by('-prioridad')
    #TODO: ordenar pro prioridad y crear campo prioridad en Speakers
    serializer_class = SpeakerSerializer

class CharlaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Charla.objects.all()
    serializer_class = CharlaSerializer

class SponsorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
