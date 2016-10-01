from slud.serializers import SpeakerSerializer, CharlaSerializer, SponsorSerializer
from rest_framework import viewsets #conjunto de vistas
from slud.models import Speaker, Charla, Sponsor
from rest_framework import permissions

class SpeakerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #
    #     else:
    #         return (permissions.IsAuthenticatedOrReadOnly(),)

class CharlaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Charla.objects.all()
    serializer_class = CharlaSerializer

class SponsorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
