from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    model = models.CharField(max_length= 100)
    year = models.IntegerField(default=2024)
    
    def __str__ (self):
        return self.name
    