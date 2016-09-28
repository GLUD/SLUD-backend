from django.conf.urls import url, include
from django.contrib import admin
from core.views import SpeakerViewSet
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'speakers', SpeakerViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include(router.urls)),
    url(r'^api/', SpeakerViewSet.as_view() )

]
