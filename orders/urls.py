from django.urls import path

from .views import SalesOrderCreateView

urlpatterns = [
    path('sales-orders/', SalesOrderCreateView.as_view(), name='sales_order'),
]
