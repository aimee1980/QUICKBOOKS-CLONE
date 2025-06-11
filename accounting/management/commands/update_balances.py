from django.core.management.base import BaseCommand
from accounting.models import Account, JournalEntry
from django.db.models import Sum

class Command(BaseCommand):
    help = 'Update account balances based on journal entries'

    def handle(self, *args, **kwargs):
        for account in Account.objects.all():
            debits = JournalEntry.objects.filter(
                account=account, entry_type='DEBIT'
            ).aggregate(total=Sum('amount'))['total'] or 0

            credits = JournalEntry.objects.filter(
                account=account, entry_type='CREDIT'
            ).aggregate(total=Sum('amount'))['total'] or 0

            if account.account_type.normal_balance == 'DEBIT':
                account.balance = debits - credits
            else:
                account.balance = credits - debits

            account.save()

        self.stdout.write(self.style.SUCCESS('✅ Account balances updated successfully.'))
