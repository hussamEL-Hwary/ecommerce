from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductCreateReadSerializer, ProductUpdateSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10


# authorization
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'create']:
            return ProductCreateReadSerializer
        elif self.action in ['update', 'partial_update']:
            return ProductUpdateSerializer
