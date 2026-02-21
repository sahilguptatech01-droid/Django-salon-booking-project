from django.db import models

# Create your models here.
class Salon(models.Model):
    name=models.CharField(max_length=50)
    adress=models.CharField(max_length=100  )
    feature=models.CharField(max_length=500)
    image=models.URLField(max_length=10000)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    date=models.DateField(auto_now=False)

    def __str__(self):
        return self.name
  
