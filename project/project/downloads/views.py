from django.shortcuts import render,redirect
from .models import games,Downloaded_Items

# Create your views here.
def show_download(request, games_id):
    game = games.objects.get(pk=games_id)
    Downloaded_Items, created = Downloaded_Items.objects.get_or_create(game=game,owner=request.owner)
    if not created:
        Downloaded_Items.quantity += 1
        Downloaded_Items.save()
        print(request, Downloaded_Items)
     
    return redirect(request, 'download.html', {'g':game})


        
