from django import forms

class HyperForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=100)
    amount = forms.IntegerField()