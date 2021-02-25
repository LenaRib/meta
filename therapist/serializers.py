from rest_framework import serializers
from .models import Psychotherapists


class TherapistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Psychotherapists
        fields = ('name', 'photo', 'metod')
