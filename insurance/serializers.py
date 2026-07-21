from .models import Customer, Policy, Lead


def customer_to_dict(customer):
    return {
        "id": customer.id,
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
        "phone_number": customer.phone_number,
        "date_of_birth": str(customer.date_of_birth),
        "account_status": customer.account_status,
    }


def policy_to_dict(policy):
    return {
        "id": policy.id,
        "policy_number": policy.policy_number,
        "policy_name": policy.policy_name,
        "policy_type": policy.policy_type,
        "premium_amount": str(policy.premium_amount),
        "coverage_term": policy.coverage_term,
        "effective_start_date": str(policy.effective_start_date),
        "customer_id": policy.customer.id,
    }


def lead_to_dict(lead):
    return {
        "id": lead.id,
        "prospect_name": lead.prospect_name,
        "contact_info": lead.contact_info,
        "referral_source": lead.referral_source,
        "lead_status": lead.lead_status,
        "assigned_agent_name": lead.assigned_agent_name,
    }