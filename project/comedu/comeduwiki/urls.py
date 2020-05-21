from django.urls import path
from . import views

urlpatterns = [
    path('', views.wiki_main, name='wiki'),
    path('<int:wiki_id>', views.wiki_detail, name='detail'),
    path('<int:wiki_id>/delete', views.wiki_delete, name='delete'),
    path('<int:wiki_id>/edit', views.wiki_edit, name='edit'),
    path('<int:wiki_id>/update', views.wiki_update, name='update'),
    path('new/', views.wiki_new, name='newwiki'),
    path('create/', views.wiki_create, name='create'),
]
