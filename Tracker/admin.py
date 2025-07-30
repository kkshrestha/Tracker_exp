from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect

admin.site.site_title = "Web Portal for Expense Tracker"
admin.site.site_header = "Expense Tracker"
admin.site.index_title = "Welcome to Milestone Expense Tracker"





# @admin.action(description='Mark selected items as Positive')
# def make_approved(modeladmin, request, queryset):
#     queryset.update(status='Positive')

# class MyModelAdmin(admin.ModelAdmin):
#     actions = [make_approved]
@admin.action(description="🔄 Refresh Page")
def refresh_page(modeladmin, request, queryset):
    # Just redirect to the same page (admin changelist view)
    return HttpResponseRedirect(request.get_full_path())

@admin.action(description = "Mark as CREDIT")
def make_CREDIT(modeladmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount < 0:
            obj.amount = obj.amount * -1
            obj.save()
    queryset.update(expense_type= "CREDIT")


@admin.action(description = "Mark as DEBIT")
def make_DEBIT(modeladmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount > 0:
            obj.amount = obj.amount * -1
            obj.save()
    queryset.update(expense_type= "DEBIT")


class TrackAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "description",
        "expense_type",
        "current_balance",
        "created_at",
        "status"
        
        
    ]
    def status(self,obj):
        if float(obj.amount) > 0:
            return f"Positive"
        else:
            return f"Negative"
    search_fields= ['expense_type','amount']
    list_filter = ['expense_type']
    actions = [make_CREDIT,make_DEBIT,refresh_page]

admin.site.register(TrackingHistory,TrackAdmin)
admin.site.register(CurrentBalance)


# Register your models here.
