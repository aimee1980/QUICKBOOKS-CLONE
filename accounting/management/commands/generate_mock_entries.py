from django.core.management.base import BaseCommand
from accounting.models import Transaction, JournalEntry, Account
from django.utils.timezone import now, timedelta
import random

class Command(BaseCommand):
    help = 'Generate mock transactions and journal entries'

    def handle(self, *args, **kwargs):
        users = set(Account.objects.values_list('user', flat=True))
        if not users:
            self.stdout.write(self.style.ERROR('⚠️ No users or accounts found. Add users and accounts first.'))
            return

        for _ in range(20):  # Create 20 mock transactions
            user_id = random.choice(list(users))
            accounts = list(Account.objects.filter(user_id=user_id))
            if len(accounts) < 2:
                continue

            debit_account, credit_account = random.sample(accounts, 2)
            amount = round(random.uniform(50.0, 500.0), 2)
            date = now().date() - timedelta(days=random.randint(1, 90))

            transaction = Transaction.objects.create(
                user=debit_account.user,
                date=date,
                description=f"Mock Transaction on {date}",
                reference_number=f"REF-{random.randint(1000, 9999)}"
            )

            JournalEntry.objects.create(
                transaction=transaction,
                account=debit_account,
                amount=amount,
                entry_type='DEBIT'
            )

            JournalEntry.objects.create(
                transaction=transaction,
                account=credit_account,
                amount=amount,
                entry_type='CREDIT'
            )

        self.stdout.write(self.style.SUCCESS('✅ 20 mock transactions with journal entries created.'))
