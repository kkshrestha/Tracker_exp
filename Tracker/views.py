from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import TrackingHistory,CurrentBalance
from django.db.models import Sum
# Create your views here.
def Index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')


        if not amount:
            messages.error(request, 'Amount is required')
            return redirect('/tracker/')
        try:
            amount = float(amount)
        except ValueError:
            messages.error(request, 'enter valid amount')
            return redirect('/tracker/')

        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)

        expense_type = 'CREDIT'
        if float(amount) < 0:
            expense_type = 'DEBIT'
        
        track_hist = TrackingHistory.objects.create(
            amount = amount,
            expense_type = expense_type,
            description = description,
            current_balance = current_balance,
           
        )
        current_balance.current_balance += float(track_hist.amount)
        current_balance.save()

        print(amount,description)
        return redirect('/tracker/')
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)

    income = 0
    expense = 0

    for transaction  in TrackingHistory.objects.all():
        if transaction.expense_type == 'DEBIT':
            expense += transaction.amount
        else:
            income += transaction.amount


    context = {
            'transaction': TrackingHistory.objects.all(),
            'current_balance': current_balance,
            'income':income,
            'expense':expense,
        }

    return render(request, 'index.html',context)

def delete_transaction(request, id):
    try:
        tracking_history = TrackingHistory.objects.get(id=id)
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

        current_balance.current_balance -= tracking_history.amount
        current_balance.save()

        tracking_history.delete()

    except TrackingHistory.DoesNotExist:
        pass  # Optionally handle the error (e.g., show a message)

    return redirect('/tracker/')


def login_view(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request,'register.html')
def forget_password(request):
    return render(request,'forgetpage.html')