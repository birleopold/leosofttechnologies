from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image1 = models.ImageField(upload_to='accessories/', null=True, blank=True)
    image2 = models.ImageField(upload_to='accessories/', null=True, blank=True)
    image3 = models.ImageField(upload_to='accessories/', null=True, blank=True)
    imahe4 = models.ImageField(upload_to='accessories/', null=True, blank=True)

    def __str__(self):
        return self.title