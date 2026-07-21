from django import forms
from .models import Customer, Policy 

from .models import Lead

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = "__all__"


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
     model = Customer
     fields = "__all__"
     widgets = {

    "first_name": forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter first name"
        }
    ),

    "last_name": forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter last name"
        }
    ),

        "email": forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@email.com"
            }
        ),

        "phone_number": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }
        ),

        "date_of_birth": forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        ),

        "account_status": forms.Select(
            attrs={
                "class": "form-select"
            }
        ),
    }
    class PolicyForm(forms.ModelForm):

     class Meta:

        model = Policy

        fields = "__all__"

        widgets = {

            "policy_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "POL-1001"
                }
            ),

            "policy_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter policy name"
                }
            ),

            "policy_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Life / Health / Vehicle"
                }
            ),

            "premium_amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter premium amount"
                }
            ),

            "coverage_term": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter years"
                }
            ),

            "effective_start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

                "customer": forms.Select(
                    attrs={
                        "class": "form-select"
                    }
                ),
            }