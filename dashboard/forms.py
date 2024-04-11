from django.forms import ModelForm
from .models import Reservation


class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
