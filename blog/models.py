from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField(max_length=500)

    content = models.TextField()

    featured_image = models.ImageField(
        upload_to='blogs/',
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blogs'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    is_featured = models.BooleanField(default=False)

    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
