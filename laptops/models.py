from django.db import models

# Create your models here.
class Laptop(models.Model):
    title = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    storage = models.IntegerField()
    ram = models.IntegerField()
    graphics = models.IntegerField()    
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    image1 = models.ImageField(upload_to='accessories/', null=True, blank=True)
    image2 = models.ImageField(upload_to='accessories/', null=True, blank=True)
    image3 = models.ImageField(upload_to='accessories/', null=True, blank=True)
    imahe4 = models.ImageField(upload_to='accessories/', null=True, blank=True)

    def __str__(self):
        return self.title