from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm

# Register your models here.

# Customise the look in admin


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity', 'issue_by']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name', 'issue_by']


admin.site.register(Stock, StockCreateAdmin)
