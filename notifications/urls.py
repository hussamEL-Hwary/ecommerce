from django.urls import path
from .views import NotificationListView, NotificationDetailView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),  # GET
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),  # GET, DELETE
]