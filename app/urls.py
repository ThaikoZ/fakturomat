from django.urls import path
from . import views


urlpatterns = [
    path('download_invoice_pdf/', views.download_invoice_pdf, name='download_invoice_pdf'),
]
