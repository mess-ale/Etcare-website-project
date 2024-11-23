from django.db import models
from django.contrib.auth.models import User


class Savings(models.Model):
    savings_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_type}"


class EqubGroup(models.Model):
    equb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    group_size = models.IntegerField()
    cycle_period = models.IntegerField()  # number of days for each cycle
    amount_per_cycle = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EqubMembership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    equb_group = models.ForeignKey(EqubGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.equb_group.name}"


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    blog_image = models.ImageField(
        upload_to='blog_images/',  # Directory to store uploaded images
        blank=False,                # Allow this field to be optional
        null=False,                 # Allow database to store NULL if no image is uploaded
        default='default.jpg'      # Default image if none is provided (optional)
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"
