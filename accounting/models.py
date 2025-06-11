# accounting/models.py
from django.db import models
from django.contrib.auth.models import User

class AccountType(models.Model):
    """Asset, Liability, Equity, Revenue, Expense"""
    name = models.CharField(max_length=50)
    normal_balance = models.CharField(max_length=6, choices=[
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit')
    ])

    def __str__(self):
        return self.name

class Account(models.Model):
    """Chart of Accounts"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account_type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.account_number} - {self.name}"

class Transaction(models.Model):
    """Double-entry transaction"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=200)
    reference_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.date} - {self.description}"

class JournalEntry(models.Model):
    """Individual debit/credit entries"""
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='entries')
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    entry_type = models.CharField(max_length=6, choices=[
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit')
    ])

    class Meta:
        verbose_name_plural = "Journal Entries"

    def __str__(self):
        return f"{self.account.name} - {self.entry_type}: ${self.amount}"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
        ('OVERDUE', 'Overdue'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='UNPAID')
    created_at = models.DateField(auto_now_add=True)
    scanned_copy = models.ImageField(upload_to='scanned_invoices/', blank=True, null=True)

    def __str__(self):
        return f"{self.client} - {self.amount} - {self.status}"
