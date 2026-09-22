from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'phone', 'email', 'service', 'preferred_date', 'preferred_time', 'birth_details', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'आपका नाम'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'मोबाइल नंबर'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ईमेल (ऐच्छिक)'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'preferred_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'birth_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'जन्म तिथि, समय और स्थान'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'अपना सवाल लिखें'}),
        }