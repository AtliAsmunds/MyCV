from typing import Callable
from django import forms

add_placeholder = lambda x: forms.TextInput(attrs={'placeholder': x})

class EmailForm(forms.Form):
    name = forms.CharField(label="", max_length=64, widget=add_placeholder('Nafn'))
    email = forms.EmailField(label="", max_length=64, widget=add_placeholder('Netfang'))
    message = forms.CharField(
        label="",
        widget=forms.Textarea( attrs={ 'placeholder': 'Skilaboð'})
        )