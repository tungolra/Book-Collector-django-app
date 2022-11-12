from django.forms import ModelForm
from .models import Format, Book

class FormatForm(ModelForm):
    class Meta: 
        model = Format
        fields = ['format', 'price']

class BookForm(ModelForm):
    class Meta: 
        model = Book
        fields = ['author', 'title', 'subtitle', 'genre', 'publish_year']