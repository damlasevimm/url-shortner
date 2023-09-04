from rest_framework import serializers
from .models import *


class URLShortenSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField(method_name='get_location')

    class Meta:
        model = URL
        fields = ['location']
        read_only_fields = ['shortcode']
    
    def get_location(self, obj):
        return '/urls/' + obj.shortcode


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url']


class URLHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'created_on']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        url_hits = URLHit.objects.filter(url_id=instance)
        representation['hits'] = len(url_hits)
        return representation