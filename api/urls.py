from django.conf.urls import url, include
from django.contrib import admin
from slud.views import SpeakerViewSet, CharlaViewSet, SponsorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'speakers', SpeakerViewSet)
router.register(r'charlas', CharlaViewSet)
router.register(r'sponsors', SponsorViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
