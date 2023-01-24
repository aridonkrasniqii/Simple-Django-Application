from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    # costum validations
    # first_name = forms.CharField(validations=[own_validator])
    class Meta:
        model = User
        # when you use all attributes just do __all__
        fields = "__all__"
