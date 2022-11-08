from django.contrib import admin
from .models import Book, Format, Subject
# Register your models here.

admin.site.register(Book)
admin.site.register(Format)
admin.site.register(Subject)