from django import forms
from .models import Cryptocurrency, Category

class CryptocurrencyForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = [
            'title', 'symbol', 'content',
            'market_cap', 'price', 'volume_24h',
            'is_active', 'category'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }