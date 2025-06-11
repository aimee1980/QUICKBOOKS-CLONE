from django.contrib.auth.models import User
from accounting.models import AccountType, Account, Transaction, JournalEntry
from datetime import date

# Create or get a test user
user, _ = User.objects.get_or_create(username='demo_user')
user.set_password('password123')
user.save()

# Create basic AccountTypes
types = {
    "Asset": AccountType.objects.get_or_create(name="Asset", normal_balance="DEBIT")[0],
    "Liability": AccountType.objects.get_or_create(name="Liability", normal_balance="CREDIT")[0],
    "Equity": AccountType.objects.get_or_create(name="Equity", normal_balance="CREDIT")[0],
    "Revenue": AccountType.objects.get_or_create(name="Revenue", normal_balance="CREDIT")[0],
    "Expense": AccountType.objects.get_or_create(name="Expense", normal_balance="DEBIT")[0],
}

# Create Accounts
accounts = {
    "Cash": Account.objects.get_or_create(user=user, name="Cash", account_type=types["Asset"], account_number="1000")[0],
    "Accounts Payable": Account.objects.get_or_create(user=user, name="Accounts Payable", account_type=types["Liability"], account_number="2000")[0],
    "Owner's Equity": Account.objects.get_or_create(user=user, name="Owner's Equity", account_type=types["Equity"], account_number="3000")[0],
    "Sales Revenue": Account.objects.get_or_create(user=user, name="Sales Revenue", account_type=types["Revenue"], account_number="4000")[0],
    "Rent Expense": Account.objects.get_or_create(user=user, name="Rent Expense", account_type=types["Expense"], account_number="5000")[0],
}

# Create sample Transactions and Journal Entries
tx1 = Transaction.objects.create(
    user=user,
    date=date(2025, 5, 1),
    description="Capital Injection",
    reference_number="TXN001"
)
JournalEntry.objects.create(transaction=tx1, account=accounts["Cash"], amount=5000, entry_type="DEBIT")
JournalEntry.objects.create(transaction=tx1, account=accounts["Owner's Equity"], amount=5000, entry_type="CREDIT")

tx2 = Transaction.objects.create(
    user=user,
    date=date(2025, 5, 5),
    description="Office Rent Payment",
    reference_number="TXN002"
)
JournalEntry.objects.create(transaction=tx2, account=accounts["Rent Expense"], amount=1000, entry_type="DEBIT")
JournalEntry.objects.create(transaction=tx2, account=accounts["Cash"], amount=1000, entry_type="CREDIT")

tx3 = Transaction.objects.create(
    user=user,
    date=date(2025, 5, 10),
    description="Sale of Services",
    reference_number="TXN003"
)
JournalEntry.objects.create(transaction=tx3, account=accounts["Cash"], amount=2000, entry_type="DEBIT")
JournalEntry.objects.create(transaction=tx3, account=accounts["Sales Revenue"], amount=2000, entry_type="CREDIT")

print("✅ Demo data populated successfully.")
