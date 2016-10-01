from slud.models import Speaker, Charla, Sponsor
from rest_framework import serializers
class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Como se muestran los datos de los modelos en el API
    """
    class Meta:
        model = Speaker
        fields = ('nombre','trabajo','foto',)

class CharlaSerializer(serializers.HyperlinkedModelSerializer):
    speakers = SpeakerSerializer(many=True)
    class Meta:
        model = Charla
        fields = ('titulo', 'descripcion', 'speakers','fecha', 'hora')

class SponsorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('logo','nombre')
