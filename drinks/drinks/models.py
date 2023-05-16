from django.db import models
class Drikns(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name