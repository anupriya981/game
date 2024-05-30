from django.shortcuts import render,redirect
from .models import history
from games.models import games
from customers.models import customer
# from .models import Gamess

def History(request,games_id):
    user=request.user
    print(user)
    data=customer.objects.get(user=user)
    print(data)
    # customers=customer.objects.filter(user)
    # customers=user.customer_profile
    history_obj,created = history.objects.get_or_create(
        owner=data,
        download_status=history.HISTORY,
        games_id=games.objects.get(pk=games_id)
    )
    return redirect(show_download)

def show_download(request):
    data=customer.objects.get(user=request.user)
    downloads=history.objects.filter(owner=data)
    print(downloads) 
    return render(request, 'download_container.html',{"downloaded":downloads})
 