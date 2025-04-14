"""
URL configuration for Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin import display
from django.urls import path

from Testovoe_app.views import ui_display
from Testovoe_app.views import html_display
from Testovoe_app.views import small_heading
from Testovoe_app.views import postF

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_page/', html_display),
    path('test_blog/', small_heading),
    path('test_UI/', ui_display),
    path('kek/<int:post_id>/', postF, name="post")
]
