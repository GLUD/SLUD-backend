from django.contrib import admin
from .models import Charla
from .models import Sponsor
from .models import Speaker
from .models import SpeakerRequest


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display=('nombre', 'trabajo')
    search_fields = ('nombre',)


@admin.register(Charla)
class CharlaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'speaker')
    search_fields = ('titulo','speakers')
    def speaker(self, obj):
        return ", ".join([p.nombre for p in obj.speakers.all()])


admin.site.register(Sponsor)


@admin.register(SpeakerRequest)
class SpeakerRequest(admin.ModelAdmin):
    list_display = ('name', 'email', 'title',)
    search_fields = ('name', 'email', 'title',)
    fields = (
        'name',
        'email',
        'title',
        'description',
    )
