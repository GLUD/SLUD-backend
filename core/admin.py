from django.contrib import admin
from core.models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Speaker)
