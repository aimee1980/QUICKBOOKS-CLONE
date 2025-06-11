"""
URL configuration for quickbooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounting import views
from django.contrib.auth import views as auth_views
from accounting.views import chat_with_gpt



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('chart-of-accounts/', views.chart_of_accounts, name='chart_of_accounts'),
    path('balance-sheet/', views.balance_sheet, name='balance_sheet'),
    path('add-transaction/', views.transaction_list, name='transaction_list'),
    path('transactions/', views.transaction_history, name='transaction_history'),
    path('profit-loss/', views.profit_and_loss, name='profit_and_loss'),
    path('profit-loss/pdf/', views.export_profit_loss_pdf, name='export_profit_loss_pdf'),
    path('profit-loss/excel/', views.export_profit_loss_excel, name='export_profit_loss_excel'),
    path('account/<int:account_id>/transactions/', views.view_account_transactions, name='view_account_transactions'),
    path('tax-docs/<str:quarter>/', views.quarterly_tax_doc, name='tax_doc'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('login/', auth_views.LoginView.as_view(template_name='accounting/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounting/logged_out.html'), name='logout'),
    path('transaction/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('api/chat/', chat_with_gpt, name='chat_with_gpt'),
    path('assistant/', views.chat_bot_view, name='chat_bot'),


]
