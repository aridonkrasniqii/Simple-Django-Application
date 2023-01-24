from django.shortcuts import render
from items.models import Item
from .forms import ItemForm, RawItemForm


# Create your views here.
def item_detail_view(request, *args, **kwargs):
    obj = Item.objects.get(id=1)
    context = {
        "title": obj.title,
        "description": obj.description,
        "summary": obj.summary,
        "price": obj.price
    }
    return render(request, 'items/item_details.html', context=context)


"""
def item_create_view(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'items/item_create.html', context=context)
"""

"""
def item_create_view(request):
    print(request.GET)
    print(request.POST)
    print(request.GET['title'])
    context = {}
    return render(request, 'items/item_create.html', context=context)

"""


def item_create_view(request):
    my_form = RawItemForm()
    if request.method == 'POST':
        my_form = RawItemForm(request.POST)
        if my_form.is_valid():
            # now the data is valid
            Item.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    my_form = RawItemForm()
    context = {
        "form": my_form
    }
    return render(request, 'items/item_create.html', context=context)
