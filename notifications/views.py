from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(ListAPIView):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer

class NotificationDetailView(RetrieveDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer