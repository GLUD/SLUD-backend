from django.shortcuts import render
from core.serializers import SpeakerSerializer
from rest_framework import viewsets #conjunto de vistas
from core.models import Speaker

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
