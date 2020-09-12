from django import forms
from .models import Stock

# Forms used to enter new Item in the store


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']
