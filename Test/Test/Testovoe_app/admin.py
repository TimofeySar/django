from django.contrib import admin
from .models import Cryptocurrency, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('title', 'symbol', 'price', 'market_cap', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'symbol')
    fieldsets = (
        (None, {
            'fields': ('title', 'symbol', 'content', 'category')
        }),
        ('Финансовые показатели', {
            'fields': ('price', 'market_cap', 'volume_24h')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )