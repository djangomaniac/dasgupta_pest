from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('decreate_order/', views.DE_create_order, name='decreate_order'),
    path('accreate_order/', views.AC_create_order, name='accreate_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('next_invoice/<int:pk>/', views.next_order, name='next_order'),
    path('<int:pk>/', views.view_order, name='view_order'),
    path('csr_pay/<int:pk>/', views.csr_pay, name='csr_pay'),
    path('amount_pay/<int:pk>/', views.amount_pay, name='amount_pay'),
    path('bank_transfer/<int:pk>/', views.bank_transfer, name='bank_transfer'),
    path('invoice/<int:pk>/', views.invoice, name='invoice'),
]
