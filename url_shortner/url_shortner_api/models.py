from django.db import models

class URL(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.headline