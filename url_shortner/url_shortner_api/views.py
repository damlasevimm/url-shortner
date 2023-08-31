from rest_framework import views, viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

from .utils import *
from .models import *
from .serializers import *


class URLAPIView(views.APIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = URLSerializer

    def get(self, request):
        queryset = URL.objects.all()
        serializer = URLSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        url=request.data.get('url')

        url_exists = URL.objects.filter(url=url)     
        if url_exists:
            return Response(URLSerializer(url_exists, many=True).data,
                            status=status.HTTP_303_SEE_OTHER)
        shortcode = create_shortcode()

        url_record = URL.objects.create(url=url, shortcode=shortcode)
        serializer = URLSerializer(url_record)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class URLHitViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = URLHitSerializer
    queryset = URLHit.objects.all()
