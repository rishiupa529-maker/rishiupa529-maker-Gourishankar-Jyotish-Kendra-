from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'आपकी बुकिंग दर्ज कर ली गई है! हम जल्द आपसे संपर्क करेंगे।')
                return redirect('booking')
            except Exception as e:
                messages.error(request, 'बुकिंग में समस्या हुई। कृपया पुनः प्रयास करें।')
                # Log the error for debugging
                print(f"Booking error: {e}")
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})