from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('ac_finance/', views.AC_finance_page, name='ac_finance'),
    path('de_finance/', views.DE_finance_page, name='de_finance'),
    path('ac_finance_detail/', views.AC_finance_detail, name='ac_finance_detail'),
    path('de_finance_detail/', views.DE_finance_detail, name='de_finance_detail'),
]
