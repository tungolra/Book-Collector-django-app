from django.forms import ModelForm
from .models import Format

class FormatForm(ModelForm):
    class Meta: 
        model = Format
        fields = ['format', 'price']