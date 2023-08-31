from django.db import models


class URL(models.Model):
    url = models.CharField(max_length=200,unique=True)
    shortcode = models.CharField(max_length=200,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

class URLHit(models.Model):
    url_id = models.ForeignKey("URL", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
