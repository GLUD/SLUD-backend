from slud.models import Speaker
from rest_framework import serializers
class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Como se muestran los datos de los modelos en el API
    """
    class Meta:
        model = Speaker
        fields = ('nombre','trabajo','foto',)
