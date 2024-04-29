from django.shortcuts import render,redirect
from .models import games,Downloaded_Items
# from .models import Gamess


# Create your views here.
def show_download(request, games_id):
    context={}
    if request.method == 'POST' and 'downloads' in request.POST:
            context['downloads'] = True
            game = request.POST.get('game')
            category = request.POST.get('category')
            rate = request.POST.get('rate')


            game = games.objects.get(pk=games_id)
            Downloaded_Items,
            created = Downloaded_Items.objects.get_or_create(game=game,owner=request.owner)
            if not created:
                Downloaded_Items.quantity += 1
                Downloaded_Items.save()
                print(request, 'game')
     
    return redirect(request, 'download_container.html', {'g':game})

