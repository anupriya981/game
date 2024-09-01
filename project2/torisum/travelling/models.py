from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=250)

class Dest_img(models.Model):
    bg_img=models.ImageField(upload_to='media')
    bg_img2=models.ImageField(upload_to='media')


class Destination_details(models.Model):
    des_place=models.CharField(max_length=200)
    des_img=models.ImageField(upload_to='media')
    des_img2=models.ImageField(upload_to='media')
    place_descrip=models.TextField(max_length=2000)
    price=models.IntegerField()

    des_place_visit1=models.TextField(max_length=1000)
    name_visit1=models.CharField( max_length=100)
    img_visit1=models.ImageField(upload_to='media')

    des_place_visit2=models.TextField(max_length=1000)
    name_visit2=models.CharField( max_length=100)
    img_visit2=models.ImageField(upload_to='media')

    des_place_visit3=models.TextField(max_length=1000)
    name_visit3=models.CharField( max_length=100)
    img_visit3=models.ImageField(upload_to='media')

    des_place_visit4=models.TextField(max_length=1000)
    name_visit4=models.CharField( max_length=100)
    img_visit4=models.ImageField(upload_to='media') 

    des_place_visit5=models.TextField(max_length=1000)
    name_visit5=models.CharField( max_length=100)
    img_visit5=models.ImageField(upload_to='media')

    des_place_visit6=models.TextField(max_length=1000)
    name_visit6=models.CharField( max_length=100)
    img_visit6=models.ImageField(upload_to='media')

class Travellers(models.Model):
    tra_img=models.ImageField(upload_to='media')
    tra_des=models.CharField(max_length=500)


