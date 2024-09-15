from django.urls import path

from . import views

urlpatterns = [
    path('purchase-orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase_order'),
]
