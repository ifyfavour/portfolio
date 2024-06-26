from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('add_service/', views.add_service, name='add_service'),
    # path('add_image/', views.add_image, name='add_image'),
]
