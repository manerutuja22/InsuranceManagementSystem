# from django.contrib import admin

# # Register your models here.
# from .models import Customer
# from .models import Policy
# from .models import Lead

# admin.site.register(Customer)
# admin.site.register(Policy)
# admin.site.register(Lead)

from django.contrib import admin
from .models import Customer, Policy, Lead


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "account_status",
    )
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("account_status",)


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = (
        "policy_number",
        "policy_name",
        "policy_type",
        "premium_amount",
        "customer",
    )
    search_fields = ("policy_number", "policy_name")
    list_filter = ("policy_type",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "prospect_name",
        "contact_info",
        "lead_status",
        "assigned_agent_name",
    )
    search_fields = ("prospect_name", "assigned_agent_name")
    list_filter = ("lead_status",)