from django.urls import path, include
from rest_framework import routers
from url_shortener_api.views import ShortenAPIView, URLHitAPIView, URLAPIView


urlpatterns = [
    path('shorten/',ShortenAPIView.as_view()),
    path('urls/<str:shortcode>/stats',URLHitAPIView.as_view()),
    path('urls/<str:shortcode>/', URLAPIView.as_view()),
]
