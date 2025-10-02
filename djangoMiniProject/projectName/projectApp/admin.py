from django.contrib import admin
from .models import FacultyDetails

admin.site.register(FacultyDetails)

from django.contrib import admin

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  search_fields = ('title', 'author', 'published_date', )
