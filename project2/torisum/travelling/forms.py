from django.forms import ModelForm
from .models import FormRegister

class FormData(ModelForm):
    class Meta:
        model = FormRegister
        fields = '__all__'
        