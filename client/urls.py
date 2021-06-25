from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('<int:pk>/', views.client_page, name='client_view'),
    path('create_client/', views.create_client, name='create_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
]
