from django.shortcuts import render
from therapist.models import Psychotherapists
from loadFromAirtable import moveAirtableToDB
from .serializers import TherapistSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TherapistViewSet(viewsets.ModelViewSet):
    moveAirtableToDB()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Psychotherapists.objects.all()
    serializer_class = TherapistSerializer

#    return render(request, 'vue.html', {"data": showall})
