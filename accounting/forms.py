# accounting/forms.py
from django import forms
from .models import Transaction, JournalEntry, Invoice

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['account', 'amount', 'entry_type']

JournalEntryFormSet = forms.inlineformset_factory(
    Transaction, JournalEntry, form=JournalEntryForm, extra=2
)

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'description', 'reference_number']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'amount', 'due_date', 'status', 'scanned_copy']
