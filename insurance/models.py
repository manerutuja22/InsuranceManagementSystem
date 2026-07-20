from django.db import models

# Create your models here.
class Customer(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    account_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Policy(models.Model):
    policy_number = models.CharField(max_length=100, unique=True)
    policy_name = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=100)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_term = models.IntegerField()
    effective_start_date = models.DateField()

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="policies"
    )

    def __str__(self):
        return self.policy_number
    
class Lead(models.Model):
    STATUS_CHOICES = [
        ("NEW", "New"),
        ("CONTACTED", "Contacted"),
        ("QUALIFIED", "Qualified"),
        ("LOST", "Lost"),
    ]

    prospect_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    referral_source = models.CharField(max_length=100)

    lead_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="NEW"
    )

    assigned_agent_name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.prospect_name
    
class AuthToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.role} - {self.token}"

class AuthToken(models.Model):
    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("AGENT", "Agent"),
    ]

    token = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.role} - {self.token}"