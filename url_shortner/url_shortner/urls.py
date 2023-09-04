from django.urls import path, include
from rest_framework import routers
from url_shortner_api.views import *


urlpatterns = [
    path('shorten/',ShortenAPIView.as_view()),
    path('urls/<str:shortcode>/stats',URLHitAPIView.as_view()),
    path('urls/<str:shortcode>/', URLAPIView.as_view()),
]
