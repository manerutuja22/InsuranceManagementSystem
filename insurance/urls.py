from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_list, name="customer_list"),
    path("add/", views.add_customer, name="add_customer"),
    path("edit/<int:id>/", views.edit_customer, name="edit_customer"),
    path("delete/<int:id>/", views.delete_customer, name="delete_customer"),
    path("policies/", views.policy_list, name="policy_list"),
    path("policies/add/", views.add_policy, name="add_policy"),
    path("policies/edit/<int:id>/", views.edit_policy, name="edit_policy"),
    path("policies/delete/<int:id>/", views.delete_policy, name="delete_policy"),
    path("leads/", views.lead_list, name="lead_list"),
    path("leads/add/", views.add_lead, name="add_lead"),
    path("leads/edit/<int:id>/", views.edit_lead, name="edit_lead"),
    path("leads/delete/<int:id>/", views.delete_lead, name="delete_lead"),
    path("api/test-auth/", views.test_auth, name="test_auth"),
    path("reports/", views.reports, name="reports"),
]