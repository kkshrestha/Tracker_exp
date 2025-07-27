from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TrackingHistory,CurrentBalance
# Create your views here.
def Index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')

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
        return redirect('/')

    return render(request, 'index.html')