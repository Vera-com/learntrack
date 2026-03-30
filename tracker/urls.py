from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.add_session, name='add_session'),
]
