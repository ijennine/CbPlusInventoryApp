import datetime

from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ProductForm(forms.Form):
    product_gtin = forms.CharField(label='Product GTIN', max_length=13, required=True, )
    product_expiry_date = forms.DateField(label='Product Expiry date', widget=DateInput, required=True, error_messages=
        {"invalid" : "Enter the product's expiry date using one of the following formats: YYYY-MM-DD or MM/DD/YYYY or MM/DD/YY"})

    def clean_product_gtin(self):
        clean_gtin = self.cleaned_data['product_gtin']

        # Check if the length of the product's gtin is 13
        if len(clean_gtin) != 13:
            raise ValidationError(_('Invalid product gtin - should be 13 numbers'))

        return clean_gtin

    def clean_product_expiry_date(self):
        clean_expiry_date = self.cleaned_data['product_expiry_date']

        # Check if product is not expired
        if clean_expiry_date < datetime.date.today():
            raise ValidationError(_('Invalid date - product already expired'))

        return clean_expiry_date


class ModifyForm(forms.Form):
    product_expiry_date = forms.DateField(label='New Product\'s Expiry date', widget=DateInput, required=True, error_messages=
        {"invalid" : "Enter the product's expiry date using one of the following formats: YYYY-MM-DD or MM/DD/YYYY or MM/DD/YY"})

    def clean_product_expiry_date(self):
        clean_expiry_date = self.cleaned_data['product_expiry_date']

        # Check if product is not expired
        if clean_expiry_date < datetime.date.today():
            raise ValidationError(_('Invalid date - product already expired'))

        return clean_expiry_date