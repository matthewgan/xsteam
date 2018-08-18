from django import forms
from .models import Vendor


class VendorCreateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        exclude = [
            'id',
            'timestamp',
            'updated',
            'isCertificated',
        ]
