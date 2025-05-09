from django.shortcuts import render, get_object_or_404
from .models import Cryptocurrency, Category

def home(request):
    categories = Category.objects.all()
    cryptocurrencies = Cryptocurrency.objects.filter(is_active=True)
    return render(request, 'Testovoe_app/crypto_list.html', {
        'cryptocurrencies': cryptocurrencies,
        'categories': categories
    })

def cryptocurrency_detail(request, pk):
    crypto = get_object_or_404(Cryptocurrency, pk=pk, is_active=True)
    return render(request, 'Testovoe_app/crypto_detail.html', {'crypto': crypto})
def about(request):
    return render(request, 'Testovoe_app/about.html')

def category_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    cryptos = Cryptocurrency.objects.filter(category=category, is_active=True)
    return render(request, 'Testovoe_app/crypto_list.html', {
        'cryptocurrencies': cryptos,
        'current_category': category,
        'categories': Category.objects.all()
    })