from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path ('people/', views.people, name='people'),
    path('people/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),

]