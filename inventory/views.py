from rest_framework.generics import ListCreateAPIView

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer


class PurchaseOrderListCreateView(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all().order_by('-created_at')
    serializer_class = PurchaseOrderSerializer
