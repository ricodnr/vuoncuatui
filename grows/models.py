from django.db import models
from sorl.thumbnail import ImageField
from io import BytesIO
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class Tata(models.Model):
    plant = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True )
    minTemp = models.BigIntegerField()
    maxTemp = models.BigIntegerField()
    minHumi = models.BigIntegerField()
    maxHumi = models.BigIntegerField()
    avatar = ImageField(upload_to='media/img/',null=True,blank=True)
    
    def __str__(self):
        return self.plant

    