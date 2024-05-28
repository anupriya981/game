from django.db import models
# Create your models here.
from customers.models import customer
from games. models import games

# data model for downloaded.
class history(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,';live'),(DELETE,'delete'))
    DOWNLOAD_STAGE=0
    DOWNLOAD=1 
    ERROR=3
    HISTORY=2   
    STATUS_CHOICE=(
        (DOWNLOAD,'download'),
        (ERROR,'error'),
        (HISTORY,'history'),
        )
    download_status = models.IntegerField(choices=STATUS_CHOICE, default=DOWNLOAD_STAGE)
    games_id=models.IntegerField()
    owner = models.ForeignKey(customer,on_delete=models.SET_NULL, null=True, related_name='downloaded')
    delete_status = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

def __str__(self):
        return f"Downloaded_Items {self.games_id} - {self.games_id.game} (Downloaded: {str(self.downloaded_dates)})"


    #model for downloded items
class Downloaded_Items(models.Model):

    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(history,on_delete=models.CASCADE,related_name='downloaded_items')
    downloaded_dates = models.DateTimeField(auto_now_add=True)
    
    


 