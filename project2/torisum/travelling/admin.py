from django.contrib import admin

# Register your models here.
from .models import register
from .models import Dest_img
from .models import Destination_details
from .models import Travellers

admin.site.register(register)
admin.site.register(Dest_img)
admin.site.register(Destination_details)
admin.site.register(Travellers)