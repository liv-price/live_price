from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.index, {'searchitem': ''}, name='home'),
    #path('<str:searchitem>', views.index, name='index'),
]

