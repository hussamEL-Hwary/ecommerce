from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

USER_MODEL = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post", "patch", "delete"]
