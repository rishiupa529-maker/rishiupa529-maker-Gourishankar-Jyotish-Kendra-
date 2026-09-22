from django.contrib import admin
from django.urls import path
from Gaurishankar_Jyotishkendra import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('service/', views.service, name='service'),

    path('gallery/', views.gallery, name='gallery'),

    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blog_list, name='blog_list'),

    path(
        'blog/<slug:slug>/',
        views.blog_detail,
        name='blog_detail'
    ),

    # Category
    path(
        'category/<slug:slug>/',
        views.category_blogs,
        name='category_blogs'
    ),

    # Featured
    path(
        'featured/',
        views.featured_blogs,
        name='featured_blogs'
    ),

    path('booking/', views.booking_view, name='booking'),
    
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)