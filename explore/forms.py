from django import forms
from .models import VehicleBooking, HotelBooking

class VehicleBookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = VehicleBooking
        fields = ['name', 'email', 'phone', 'vehicle_type', 'pickup_location', 'drop_location', 'booking_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-control'}),
            'drop_location': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ["name", "email"]