from django.db import models


class CurrentBalance(models.Model):
    current_bal = models.FloatField(default = 0)


class Expense_track(models.Model):
    current_bal = models.ForeignKey(CurrentBalance, on_delete= models.CASCADE)
    amount = models.FloatField()
    exp_type = models.CharField(choices =( ('DR','Dr'),('CR','Cr')),max_length = 200)
    description = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
