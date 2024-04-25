from django.shortcuts import render
from . models import games
from django.http import JsonResponse

def index(request):
    # Some processing
    # feature_product=games.objects.order_by('priority') 
    return render(request, 'index.html')

# # def list_games(request):
# #     """_summary_
# #     returns games list page
# #     args:
# #         request (_type_): _description_
# #     Returns:
# #         _type_: _description_
# #     """
# #     games_list=games.objects.get(id=game_list-id)
# #     context={"games": games_list}
# #     return render(request, 'games_details.html',context)

def list_games(request):
    # games_list=games.objects.get(pk=pk)
    # context={"games": games_list}
    return render(request, 'games.html')


def description(request):
    return render(request, 'games_description_car.html')

def description_bird(request):
    return render(request, 'game_descr_bird.html')

def description_cand(request):
    return render(request, 'game_descr_cand.html')


def game_list(request):
    return render(request, 'games_list_page.html')









