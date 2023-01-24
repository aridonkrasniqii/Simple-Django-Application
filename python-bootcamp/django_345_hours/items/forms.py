from django import forms
from items.models import Item

""" 
class ItemForm(): 
    pass 
class ItemModelForm(): 
    pass 
"""


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # models fields
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]


class RawItemForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

