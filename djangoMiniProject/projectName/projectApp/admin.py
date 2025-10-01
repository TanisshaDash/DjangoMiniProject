from django.contrib import admin
from .models import FacultyDetails

admin.site.register(FacultyDetails)

from django.contrib import admin

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('available', 'published_date')