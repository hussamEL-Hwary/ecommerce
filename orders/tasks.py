from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from orders.constants import NotificationsConstants
from notifications.models import Notification
from products.models import Product


@shared_task
def notify_low_stock():
    """
    Celery task that checks for products with stock below the threshold
    and creates a notification if none exists for that product with is_read=False
    or if the last notification was created more than 3 days ago.
    """
    low_stock_products = Product.objects.filter(stock__lt=NotificationsConstants.LOW_STOCK_LIMIT)
    three_days_ago = timezone.now() - timedelta(days=NotificationsConstants.RENOTIFY_AGE_LIMIT)

    for product in low_stock_products:
        # Check if there is a notification with is_read=False
        recent_notification = Notification.objects.filter(
            product=product,
            created_at__gte=three_days_ago
        ).first()

        # Create a notification if no recent unread notifications exist
        if not recent_notification or recent_notification.is_read:
            Notification.objects.create(
                product=product,
                message=f"Stock for {product.name} is low: {product.stock} remaining."
            )
