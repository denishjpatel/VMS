from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from purchases.models import PurchaseOrder
from django.db.models import Avg, F, ExpressionWrapper, fields

@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.delivery_date:
        vendor = instance.vendor
        total_completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        on_time_deliveries = PurchaseOrder.objects.filter(
            vendor=vendor,
            status='completed',
            delivery_date__gte=timezone.now()
        ).count()
        if total_completed_pos > 0:
            on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100
            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        vendor = instance.vendor
        new_avg = PurchaseOrder.objects.filter(
            vendor=vendor, 
            status='completed'
        ).aggregate(Avg('quality_rating'))['quality_rating__avg']
        vendor.quality_rating_avg = new_avg if new_avg is not None else 0.0
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date:
        vendor = instance.vendor
        average_response_time = PurchaseOrder.objects.filter(
            vendor=vendor,
            acknowledgment_date__isnull=False
        ).aggregate(
            avg_response_time=Avg(
                ExpressionWrapper(
                    F('acknowledgment_date') - F('issue_date'),
                    output_field=fields.DurationField()
                )
            )
        )['avg_response_time']

        print(average_response_time)
        # Convert timedelta to seconds
        if average_response_time is not None:
            average_response_time_seconds = average_response_time.total_seconds()
        else:
            average_response_time_seconds = 0

        vendor.average_response_time = average_response_time_seconds
        vendor.save()
        


@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    print("called")
    if instance.status:
        print("inside if")
        vendor = instance.vendor
        total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
        print("total pos", total_pos)
        fulfilled_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').exclude(quality_rating__isnull=True).count()
        print("fulfilled pos", fulfilled_pos)
        if total_pos > 0:
            print("inside if2")
            fulfillment_rate = (fulfilled_pos / total_pos) * 100
            print("fulfillment rate", fulfillment_rate)
            vendor.fulfillment_rate = fulfillment_rate
            vendor.save()
            print("vendor saved")
