# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .form import CustomerForm

from .models import Policy
from .form import PolicyForm

import json
from django.http import JsonResponse
from .serializers import customer_to_dict

from .models import Lead
from .form import LeadForm

from django.db.models import Sum, Count

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer_list.html", {"customers": customers})


def add_customer(request):
    if request.method == "POST":
        print("POST DATA:", request.POST)

        form = CustomerForm(request.POST)

        if form.is_valid():
            customer = form.save()
            print("SAVED CUSTOMER:", customer.id, customer.email)
            return redirect("customer_list")
        else:
            print("FORM ERRORS:", form.errors)

    else:
        form = CustomerForm()

    return render(request, "customer_form.html", {"form": form})


def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:
        form = CustomerForm(instance=customer)

    return render(request, "customer_form.html", {"form": form})


def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    customer.delete()

    return redirect("customer_list")

def policy_list(request):
    policies = Policy.objects.all()
    return render(request, "policy_list.html", {"policies": policies})


def add_policy(request):
    if request.method == "POST":
        form = PolicyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("policy_list")

    else:
        form = PolicyForm()

    return render(request, "policy_form.html", {"form": form})


def edit_policy(request, id):
    policy = get_object_or_404(Policy, id=id)

    if request.method == "POST":
        form = PolicyForm(request.POST, instance=policy)

        if form.is_valid():
            form.save()
            return redirect("policy_list")

    else:
        form = PolicyForm(instance=policy)

    return render(request, "policy_form.html", {"form": form})


def delete_policy(request, id):
    policy = get_object_or_404(Policy, id=id)
    policy.delete()

    return redirect("policy_list")


from django.http import JsonResponse
def test_auth(request):
    return JsonResponse({
        "message": "Authentication successful",
        "role": request.user_role
    })

from .models import Lead
from .form import LeadForm
def lead_list(request):
    leads = Lead.objects.all()

    return render(
        request,
        "lead_list.html",
        {"leads": leads}
    )


def add_lead(request):

    if request.method == "POST":

        form = LeadForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lead_list")

    else:
        form = LeadForm()

    return render(
        request,
        "lead_form.html",
        {"form": form}
    )


def edit_lead(request, id):

    lead = get_object_or_404(Lead, id=id)

    if request.method == "POST":

        form = LeadForm(
            request.POST,
            instance=lead
        )

        if form.is_valid():
            form.save()
            return redirect("lead_list")

    else:

        form = LeadForm(
            instance=lead
        )

    return render(
        request,
        "lead_form.html",
        {"form": form}
    )


def delete_lead(request, id):

    lead = get_object_or_404(
        Lead,
        id=id
    )

    lead.delete()

    return redirect("lead_list")

def reports(request):

    total_customers = Customer.objects.count()

    active_customers = Customer.objects.filter(
        account_status="ACTIVE"
    ).count()

    inactive_customers = Customer.objects.filter(
        account_status="INACTIVE"
    ).count()

    total_policies = Policy.objects.count()

    total_premium = Policy.objects.aggregate(
        total=Sum("premium_amount")
    )["total"] or 0

    total_leads = Lead.objects.count()

    lead_status = Lead.objects.values(
        "lead_status"
    ).annotate(
        count=Count("id")
    )

    policy_types = Policy.objects.values(
        "policy_type"
    ).annotate(
        count=Count("id")
    )

    context = {
        "total_customers": total_customers,
        "active_customers": active_customers,
        "inactive_customers": inactive_customers,
        "total_policies": total_policies,
        "total_premium": total_premium,
        "total_leads": total_leads,
        "lead_status": lead_status,
        "policy_types": policy_types,
    }

    return render(request, "reports.html", context)
