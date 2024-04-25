from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    # phone_no = models.PhoneNumberField()
    phone= models.CharField(max_length=20)
    # phone_no=models.IntegerField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


def __str__(self) -> str:
    return self.title   