# doctors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('doc1/', views.doc1, name='doc1'),
    path('doc2/', views.doc2, name='doc2'),
    path('doc3/', views.doc3, name='doc3'),
]
