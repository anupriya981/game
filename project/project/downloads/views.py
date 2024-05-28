from django.shortcuts import render,redirect
from .models import history
from games.models import games
from customers.models import customer
# from .models import Gamess

def History(request):
    user=request.user
    print(user)
    data=customer.objects.get(user=user)
    print(data)
    # customers=customer.objects.filter(user)
    # customers=user.customer_profile
    history_obj,created = history.objects.get_or_create(
        owner=data,
        download_status=history.HISTORY
    )
    return redirect(show_download)

def show_download(request):
    # if request.POST:        
    #         user = request.user
    #         customer= user.customer_profile 
    #         quantity = int(request.POST.get('quantity'))
    #         games_id = request.POST.get('games_id ')
    #         history_obj, created = history.objects.get_or_create(
    #             owner = customer,
    #             download_status = history.HISTORY
    #         )
            # game=games.objects.get(pk=games_id)
    #         Downloaded_items = Downloaded_Items.objects.create(
    #              games_id=games_id,
    #              owner=history_obj, 
    #              quantity=quantity,
    #             #  downloaded_date=downloaded_date,
    #    
    #      )
    game=games.objects.all()
    data=customer.objects.get(user=request.user)
    downloads=history.objects.filter(owner=data)
    print(downloads)

    return render(request, 'download_container.html',{'downloaded':downloads})

 