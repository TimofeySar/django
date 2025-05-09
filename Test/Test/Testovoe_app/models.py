from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Cryptocurrency(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название криптовалюты")
    symbol = models.CharField(max_length=10, verbose_name="Символ")
    content = models.TextField(blank=True, verbose_name="Описание")
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Рыночная капитализация (USD)")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Цена (USD)")
    volume_24h = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Объем торгов за 24ч (USD)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.title} ({self.symbol})"

    class Meta:
        verbose_name = "Криптовалюта"
        verbose_name_plural = "Криптовалюты"