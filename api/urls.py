from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from slud.views import SpeakerViewSet
from slud.views import CharlaViewSet
from slud.views import SponsorViewSet
from slud.views import home
from slud.views import SpeakerAPIView


router = routers.DefaultRouter()
router.register(r'speakers', SpeakerViewSet)
router.register(r'charlas', CharlaViewSet)
router.register(r'sponsors', SponsorViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^talk/$', SpeakerAPIView.as_view()),
    url(r'^$', home),
]
