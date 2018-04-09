from slud.serializers import SpeakerSerializer, CharlaSerializer, SponsorSerializer
from rest_framework import viewsets
from rest_framework import status
from slud.models import Speaker, Charla, Sponsor
from rest_framework import permissions
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse

from .models import SpeakerRequest
from .forms import SpeakerRequestModelForm



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


class SpeakerAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        form = SpeakerRequestModelForm(request.data)
        if form.is_valid():
            form.save()

        return JsonResponse({'ok': True})

        # return Response()
