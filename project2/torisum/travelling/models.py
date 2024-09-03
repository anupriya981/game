from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=200)
    yor_aplace=models.CharField(max_length=250)


class Dest_img(models.Model):
    bg_img=models.ImageField(upload_to='media')
    bg_img2=models.ImageField(upload_to='media')


class Destination_details(models.Model):
    des_place=models.CharField(max_length=200)
    des_img=models.ImageField(upload_to='media')
    des_img2=models.ImageField(upload_to='media')
    place_descrip=models.TextField(max_length=2000)
    price=models.IntegerField()

class Travellers(models.Model):
    tra_img=models.ImageField(upload_to='media')
    tra_des=models.CharField(max_length=500)

class VisitPlace(models.Model):

    des_place_visit=models.TextField(max_length=1000)
    name_visit=models.CharField( max_length=100)
    img_visit=models.ImageField(upload_to='media')
