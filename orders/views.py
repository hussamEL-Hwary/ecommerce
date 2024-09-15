from rest_framework.generics import CreateAPIView

from .models import SalesOrder
from .serializers import SalesOrderSerializer


class SalesOrderCreateView(CreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
