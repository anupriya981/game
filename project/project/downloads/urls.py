from django.urls import path
from . import views 
# from . views  import downloads

urlpatterns = [   
    path('history', views.History, name='history'), 
    # path('download/<int:games_id>',views.show_download,name='downloads'),
    path('download',views.show_download,name='downloads')
]

