from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('<int:pk>/', views.client_page, name='client_view'),
    path('sub_client/<int:pk>/', views.sub_client_page, name='sub_client_page'),
    path('detail/<int:pk>/', views.client_detail_page, name='client_detail_view'),
    path('invoice/<int:pk>/', views.invoice_detail_page, name='invoice_detail_view'),
    path('create_client/', views.create_client, name='create_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
    path('create_sub_client/', views.create_sub_client, name='create_sub_client'),
    path('update_sub_client/<int:pk>/', views.update_sub_client, name='update_sub_client'),
]
