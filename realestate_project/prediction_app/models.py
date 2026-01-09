from django.db import models

class Property(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    stories = models.IntegerField()
    parking = models.IntegerField()

    mainroad = models.CharField(max_length=5)
    guestroom = models.CharField(max_length=5)
    basement = models.CharField(max_length=5)
    hotwaterheating = models.CharField(max_length=5)
    airconditioning = models.CharField(max_length=5)
    prefarea = models.CharField(max_length=5)
    furnishingstatus = models.CharField(max_length=20)

    prediction = models.FloatField(null=True)

    def __str__(self):
        return f"Pred: {self.prediction}"
