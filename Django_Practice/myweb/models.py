from django.db import models

# Create your models here.
class ITEM(models.Model):
    itemid=models.CharField(max_length=50,primary_key=True)
    itemnam=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=50)
    pictureurl=models.CharField(max_length=50)
    def __str__(self):
        return self.itemnam