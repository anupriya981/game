from django.db import models

# Create your models here.
from customers.models import customer
from games. models import games

# data model for downloaded.
class history(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,';live')),(DELETE,'delete')
    DOWNLOAD_STAGE=0
    DOWNLOAD=1
    ERROR=3
    HISTORY=2
    
    STATUS_CHOICE=((DOWNLOAD,'download')),((ERROR,'error')),((HISTORY,'history'))
    download_status=models.IntegerField(choices=STATUS_CHOICE,default =DOWNLOAD_STAGE)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='downloads')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    #model for downloded items
class Downloaded_Items(models.Model):
    quantity=models.IntegerField(default=1)
    games=models.ForeignKey(games,related_name='downloaded_history',on_delete=models.SET_NULL,null=True,)

    game=models.CharField(max_length=250)
    img=models.ImageField(upload_to='media/')
    category=models.CharField(max_length=20)
    rate=models.FloatField()
    priority=models.IntegerField(default=0)

    owner=models.ForeignKey(history,on_delete=models.CASCADE,related_name='downloaded_items')

