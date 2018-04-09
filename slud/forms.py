from django import forms

from .models import SpeakerRequest

class SpeakerRequestModelForm(forms.ModelForm):
    class Meta:
        model = SpeakerRequest
        fields = (
            'name',
            'email',
            'title',
            'description',
        )
