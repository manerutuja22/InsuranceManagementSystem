from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .form import CustomerForm

from .models import Policy
from .form import PolicyForm

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