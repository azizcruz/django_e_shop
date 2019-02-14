from django import forms

class WishlistForm(forms.Form):
    product_id = forms.CharField(required=True, widget=forms.HiddenInput)
