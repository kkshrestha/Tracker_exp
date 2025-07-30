from django.urls import path

from .import views

urlpatterns  = [
    path('',views.Index,name='home'),
    path('delete-tracking_history/<id>/', views.delete_transaction,name="delete_transaction"),
]

