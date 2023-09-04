from rest_framework import views, status
from rest_framework.response import Response
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

import hashlib

from .models import *
from .serializers import *


class ShortenAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = URLSerializer

    def get(self, request):
        queryset = URL.objects.all()
        serializer = URLSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        url=request.data.get('url')
 
        try:
            url_exists = URL.objects.get(url=url)
        except URL.DoesNotExist:
            url_exists = None  
        if url_exists:
            URLHit.objects.create(url_id=url_exists)
            return Response(URLShortenSerializer(url_exists).data,
                            status=status.HTTP_303_SEE_OTHER)

        shortcode = hashlib.shake_256(url.encode()).hexdigest(5)
        
        url_record = URL.objects.create(url=url, shortcode=shortcode)
        serializer = URLShortenSerializer(url_record)
        URLHit.objects.create(url_id=url_record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class URLAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = URLSerializer

    def get(self, request, shortcode):
        queryset = URL.objects.get(shortcode=shortcode)
        serializer = URLSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_307_TEMPORARY_REDIRECT)


class URLHitAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = URLHitSerializer

    def get(self, request, shortcode):
        queryset = URL.objects.get(shortcode=shortcode)
        serializer = URLHitSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
