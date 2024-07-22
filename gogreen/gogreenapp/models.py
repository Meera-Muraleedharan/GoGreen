from django.db import models

# Create your models here.
class Item(models.Model):
    img=models.ImageField(upload_to='pic')
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    spec = models.CharField(max_length=50)

class Meta:
    

    def __str__(self):
        return self.name