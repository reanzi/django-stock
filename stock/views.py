from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockCreateForm, StockSearchForm

# Create your views here.


def home(request):
    header = 'Welcome: This is the Home Page'
    context = {
        "header": header,
    }
    return render(request, "home.html", context)


def list_items(request):
    header = 'List of Items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "items": queryset,
        'form': form
    }
    # Seaching
    if request.method == 'POST':
        queryset = Stock.objects.filter(
            category__icontains=form['category'].value())
        # item_name__icontains=form['item_name'].value())
        print(queryset)
        context = {
            'form': form,
            'header': header,
            'queryset': queryset,
        }

        # print(context)
    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_items')  # redirect(name)
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)
