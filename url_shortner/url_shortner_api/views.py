from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import *
from .serializers import *

class URLViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = URLSerializer
    queryset = URL.objects.all()