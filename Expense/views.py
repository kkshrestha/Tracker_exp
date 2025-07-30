from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import CurrentBalance, Expense_track
# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        print(description, amount)
        now = timezone.localtime(timezone.now())
        print(now)

        Obj, created = CurrentBalance.objects.get_or_create(id=1)

        exp_type = 'Cr'
        if float(amount) >= 0:
            exp_type = 'Dr'
        exp_his =Expense_track.objects.create(
            amount = amount,
            description = description,
            current_bal = Obj,
            exp_type = exp_type,
        )
        Obj.current_bal += float(exp_his.amount)
        Obj.save()
        return redirect('/expense/')
    return render(request,'home.html')

