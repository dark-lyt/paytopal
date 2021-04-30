from django import forms


class PayForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)
