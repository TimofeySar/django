from django.contrib import admin
from django.urls import path
from Testovoe_app.views import (
    home,
    cryptocurrency_detail,
    category_view,
    about
)

urlpatterns = [
    path('', home, name='home'),
    path('crypto/<int:pk>/', cryptocurrency_detail, name='cryptocurrency_detail'),
    path('category/<int:category_id>/', category_view, name='category_view'),
    path('about/', about, name='about'),
]