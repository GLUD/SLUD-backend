from core.serializers import SpeakerSerializer
from rest_framework import viewsets #conjunto de vistas
from core.models import Speaker
from core.permissions import LoginOrReadOnly
from rest_framework import permissions

class SpeakerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes

class SpeakerViewSet(APIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    @api_view(['GET'])
    @permission_classes((AllowAny,))
    def get(self, request, format=None):
        content = {
        'encoding': 'UTF-8',
        'status': 'OK'
    }
        return Response(content)

    @api_view(['POST'])
    @authentication_classes((SessionAuthentication, BasicAuthentication))
    @permission_classes((IsAuthenticated,))
    def post(self, request, format=None):
        content = {
            'user': str(request.user),  # django.contrib.auth.User instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
