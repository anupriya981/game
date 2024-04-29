from django.shortcuts import render
from . models import games

def index(request):
    # Some processing
    # feature_product=games.objects.order_by('priority') 
    return render(request, 'index.html')

def list_games(request):
    """_summary_
    returns games list page
    args:
        request (_type_): _description_
    Returns:
        _type_: _description_
    """
    # games_list=games.objects.all()
    # context={"games": games_list}
    return render(request, 'games.html')

def detail_games(request,pk):
    game=games.objects.get(pk=pk)
    context={' game':game}
    return render(request, 'games.html',context)

def description(request):
    return render(request, 'games_description_car.html')

def description_bird(request):
    return render(request, 'game_descr_bird.html')

def description_cand(request):
    return render(request, 'game_descr_cand.html')

def description_sub(request):
    return render(request, 'game_des_sub.html')

def game_list(request):
    return render(request, 'games_list_page.html')









