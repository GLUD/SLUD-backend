from django.contrib import admin
from slud.models import Speaker, Charla

class SpeakerAdmin(admin.ModelAdmin):
    list_display=('nombre', 'trabajo')
    search_fields = ('nombre',)

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Charla)
