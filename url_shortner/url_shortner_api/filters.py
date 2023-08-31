from django_filters import rest_framework as DjangoFilterBackend
from .models import *

class URLFilter(DjangoFilterBackend):
    class Meta:
        model = URL
        fields = '__all__'