from django import forms
from .models import Customer,Policy


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = "__all__"

        widgets = {
            "effective_start_date": forms.DateInput(
                attrs={"type": "date"}
            )
        }