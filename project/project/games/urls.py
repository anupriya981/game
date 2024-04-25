
from django.urls import path
# from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('games_list',views.list_games,name='games'),
    # path('games_list_page',views.game_list,name='games_list_page'),
   
    path('games_description_car',views.description,name='games_description_car'),

    path('game_descr_bird',views.description_bird,name='game_descr_bird'),
    path('game_descr_cand',views.description_cand,name='game_descr_cand'),

]
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
