from django.shortcuts import render
from . models import games
from django.contrib.auth.decorators import login_required

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

# def description(request):
#     return render(request, 'games_description_car.html')

# def description_bird(request):
#     return render(request, 'game_descr_bird.html')

# def description_cand(request):
#     return render(request, 'game_descr_cand.html')

# def description_sub(request):
#     return render(request, 'game_des_sub.html')

# def description_ludo(request):
#     return render(request, 'game_des_ludo.html')

# def description_mario(request):
#     return render(request, 'game_des_mario.html')

# def description_motor(request):
#     return render(request, 'game_des_motor.html')

# def description_gtav(request):
#     return render(request, 'game_des_gta.html')


@login_required(login_url = 'login/')
def game_list(request):
    g=games.objects.all()
    context={'games':g}
    return render(request, 'games_list_page.html',context)









