from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # एडमिन पैनल की लिस्ट में कौन-कौन से कॉलम दिखेंगे
    list_display = ('full_name', 'phone', 'service', 'preferred_date', 'preferred_time', 'created_at')
    
    # राइट साइड में फ़िल्टर (Filter) का ऑप्शन
    list_filter = ('service', 'preferred_date')
    
    # नाम, फोन या ईमेल से सर्च करने का बॉक्स
    search_fields = ('full_name', 'phone', 'email')