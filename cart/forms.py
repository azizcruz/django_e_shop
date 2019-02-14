from django import forms

class CartForm(forms.Form):

    quantity = forms.IntegerField(min_value=1)
    update = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
