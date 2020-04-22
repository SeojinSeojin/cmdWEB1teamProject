from django.urls import path
from . import views

urlpatterns=[
    path('',views.gradu_index,name='grad_index'),
    path('cal',views.gradu_cal, name ='gradu_cal'),
    path('cal/calculate',views.calculate, name='calculate'),
    path('cal/result',views.gradu_result,name='gradu_result'),
]

    