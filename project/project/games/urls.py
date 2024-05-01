
from django.urls import path
# from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    # path('list_game/<int:p>', views.list_games, name='games'),
    # path('list_game/<int:p>/', views.game_list, name='list_game')

    path('games_list/<int:p>',views.list_games,name='games'),
    # path('games_detail/<pk>',views.list_games,name='detail_games'),
  
    path('detail_games/<pk>',views.detail_games,name='details_games'),  
    path('games_list_page',views.game_list,name='games_list_page'),


    path('games_description_car',views.description,name='games_description_car'),
    path('game_descr_bird',views.description_bird,name='game_descr_bird'),
    path('game_descr_cand',views.description_cand,name='game_descr_cand'),
    path('game_descr_sub',views.description_sub,name='game_des_sub'),
    path('game_descr_ludo',views.description_ludo,name='game_des_ludo'),
    path('game_descr_mario',views.description_mario,name='game_des_mario'),
    path('game_descr_motor',views.description_motor,name='game_des_moto'),
    path('game_descr_gta',views.description_gtav,name='game_des_gta'),

]
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
