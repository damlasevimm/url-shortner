from rest_framework import serializers
from .models import *

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'

class URLHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLHit
        fields = '__all__'