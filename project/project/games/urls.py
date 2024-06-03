
from django.urls import path
# from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.Home,name='index'),
    path('',views.index,name='home'),
    path('games_list/<int:p>',views.list_games,name='games'),
    path('detail_games/<pk>',views.detail_games,name='details_games'),  
    path('games_list_page',views.game_list,name='games_list_page'),
    
    path('search/', views.search_venues, name='search'),
]

