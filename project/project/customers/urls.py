from django.urls import path
# from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    path('account',views.show_account,name='account'),
    path('login',views.user_login,name='login'),
    path('logout',views.sign_out,name='logout'),

]