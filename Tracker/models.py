from django.db import models
from django.contrib.auth.models import User

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default =0)

    def __str__(self):
        return f"{self.current_balance}"

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete = models.CASCADE)
    amount = models.FloatField(editable = False)
    expense_type = models.CharField(choices = (('CREDIT','CREDIT'),('DEBIT','DEBIT')),max_length = 200)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)



    def __str__(self):
        return f"The amount is {self.amount} and the description is \"{self.description}\" and the type of expense is {self.expense_type}"
# Create your models here.
