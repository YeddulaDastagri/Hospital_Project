from app.views import *  
from django.urls import path 


urlpatterns = [
    path('crdiologist/', cardiologist,name='cardiologist'), 
    path('dermatologist/',dermatologist,name='dermatologist'),
]