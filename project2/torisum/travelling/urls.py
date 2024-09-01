
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('registration',views.Register,name='registration'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('tra_des/<pk>',views.Tra_des, name='tra_des'),
]