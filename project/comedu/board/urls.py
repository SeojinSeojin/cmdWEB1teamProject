from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_main, name='board'),
    path('<int:post_id>', views.board_detail, name='detail'),
    path('<int:post_id>/delete', views.board_delete, name='delete'),
    path('<int:post_id>/edit', views.board_edit, name='edit'),
    path('<int:post_id>/update', views.board_update, name='update'),
    path('new/', views.board_new, name='newPost'),
    path('create/', views.board_create, name='create'),
]
