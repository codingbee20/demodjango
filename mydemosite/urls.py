from django.urls import path
from mydemosite import views

urlpatterns = [
    path('', views.mydemosite, name='mydemosite')
]