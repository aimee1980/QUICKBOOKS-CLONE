from django.contrib import admin
from .models import AccountType, Account, Transaction, JournalEntry

class JournalEntryInline(admin.TabularInline):
    model = JournalEntry
    extra = 2  # Shows 2 empty forms by default

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    inlines = [JournalEntryInline]
    list_display = ('date', 'description', 'reference_number')

admin.site.register(AccountType)
admin.site.register(Account)