from .views import *
from django.urls import path

urlpatterns=[
    path('service',ServiceApi.as_view()),
    path('serviceId/<pk>',ServiceIdApi.as_view()),
    path('invoice',InvoiceApi.as_view()),
    path('invoiceId/<pk>',InvoiceIdApi.as_view()),

]