from rest_framework import serializers
import re

from .models import URL, URLHit


class URLShortenSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField(method_name='get_location')

    class Meta:
        model = URL
        fields = ['location']
        read_only_fields = ['shortcode']

    def validate_url(self, url):
        regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

        regex_compile = re.compile(regex)

        if(re.search(regex_compile, url)):
            return url
        else:
            raise serializers.ValidationError('URL has a wrong format!')
    
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
