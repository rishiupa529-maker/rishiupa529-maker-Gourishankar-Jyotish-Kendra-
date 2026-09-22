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

    blogs = Blog.objects.filter(
        status='published'
    ).select_related(
        'author',
        'category'
    )

    categories = Category.objects.all()

    # Search
    search = request.GET.get('search')

    if search:
        blogs = blogs.filter(
            Q(title__icontains=search) |
            Q(short_description__icontains=search) |
            Q(content__icontains=search)
        )

    # Category filter
    category_slug = request.GET.get('category')

    if category_slug:
        blogs = blogs.filter(
            category__slug=category_slug
        )

    # Featured blogs
    featured_blogs = Blog.objects.filter(
        status='published',
        is_featured=True
    ).select_related(
        'author',
        'category'
    )[:5]

    context = {
        'blogs': blogs,
        'categories': categories,
        'featured_blogs': featured_blogs,
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

    blog = get_object_or_404(
        Blog.objects.select_related(
            'author',
            'category'
        ),
        slug=slug,
        status='published'
    )

    # Increase views
    blog.views += 1
    blog.save(update_fields=['views'])

    # Related blogs
    related_blogs = Blog.objects.filter(
        status='published',
        category=blog.category
    ).exclude(
        id=blog.id
    ).select_related(
        'author',
        'category'
    )[:4]

    context = {
        'blog': blog,
        'related_blogs': related_blogs,
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