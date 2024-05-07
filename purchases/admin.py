from django.contrib import admin
from .models import PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'po_number', 'status', 'quality_rating')

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
