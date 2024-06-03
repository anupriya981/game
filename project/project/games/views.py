from django.shortcuts import render
from . models import games
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

def Home(request):
    print(request.user)

    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def list_games(request,p):
    """_summary_
    returns games list page
    args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    games_list=games.objects.get(pk=p)
    context={"games": games_list}
    return render(request, 'games_descriptions.html',context)

def detail_games(request,p): 
    game=games.objects.order_by('priority')
    context={'games':game}
    return render(request, 'games_details.html')

@login_required(login_url = 'login/')
def game_list(request):
    g=games.objects.all()
    context={'games':g}
    return render(request, 'games_list_page.html',context)

def search_venues(request):
    query = request.GET.get('q')
    if query:
        results = games.objects.filter(game=query)
        results = games.objects.annotate(lower_game=Lower('game')).filter(lower_game__icontains=query.lower())

    else:
         results = games.objects.none()  
    return render(request, 'search_venues.html', {'results': results})







