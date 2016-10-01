from django.contrib import admin
from slud.models import Speaker, Charla, Sponsor

class SpeakerAdmin(admin.ModelAdmin):
    list_display=('nombre', 'trabajo')
    search_fields = ('nombre',)

class CharlaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'speaker')
    search_fields = ('titulo','speakers')
    def speaker(self, obj):
        return ", ".join([p.nombre for p in obj.speakers.all()])

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Charla, CharlaAdmin)
admin.site.register(Sponsor)
