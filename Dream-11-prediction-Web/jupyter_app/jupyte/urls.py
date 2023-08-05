
from django.urls import path
from . import views

app_name = 'jupyte'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index,name='index'),
    path('process_players/', views.process_players, name='process_players'),
    path('contact/', views.contact,name='contact'),]
