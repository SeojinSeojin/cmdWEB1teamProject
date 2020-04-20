"""comedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import board.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.main, name='main'),
    path('board/', board.views.board_main, name='board'),
    path('board/<int:post_id>', board.views.board_detail, name='detail'),
    path('board/<int:post_id>/delete', board.views.board_delete, name='delete'),
    path('board/new/', board.views.board_new, name='newPost'),
    path('board/create/', board.views.board_create, name='create'),
]
