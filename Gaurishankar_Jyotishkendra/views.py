from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from booking.forms import BookingForm 




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')


from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from blog.models import Blog, Category


def blog_list(request):
    """
    Show all published blogs
    """
    # For now, return empty data to avoid database connection issues
    # TODO: Re-enable database queries once MySQL connection is stable
    context = {
        'blogs': [],
        'categories': [],
        'featured_blogs': [],
    }

    return render(
        request,
        'blog_list.html',
        context
    )


def blog_detail(request, slug):
    """
    Show single blog
    """
    # For now, return empty data to avoid database connection issues
    # TODO: Re-enable database queries once MySQL connection is stable
    context = {
        'blog': None,
        'related_blogs': [],
    }

    return render(
        request,
        'blog_detail.html',
        context
    )


def category_blogs(request, slug):
    """
    Show blogs according to category
    """
    try:
        category = get_object_or_404(
            Category,
            slug=slug
        )

        blogs = Blog.objects.filter(
            category=category,
            status='published'
        ).select_related(
            'author',
            'category'
        )

        categories = Category.objects.all()

        context = {
            'category': category,
            'blogs': blogs,
            'categories': categories,
        }
    except Exception as e:
        # Fallback if database connection fails
        context = {
            'category': None,
            'blogs': [],
            'categories': [],
        }

    return render(
        request,
        'category_blogs.html',
        context
    )


def featured_blogs(request):
    """
    Show only featured blogs
    """

    blogs = Blog.objects.filter(
        status='published',
        is_featured=True
    ).select_related(
        'author',
        'category'
    )

    context = {
        'blogs': blogs,
    }

    return render(
        request,
        'blogs/featured_blogs.html',
        context
    )

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'आपकी बुकिंग दर्ज कर ली गई है! हम जल्द आपसे संपर्क करेंगे।')
            return redirect('booking')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})