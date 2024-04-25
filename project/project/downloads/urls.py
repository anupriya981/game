from django.urls import path
from . import views 
# from . views  import downloads

urlpatterns = [


    path('show_download/<int:games_id>/', views.show_download, name='show_download'),

]

