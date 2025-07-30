from django.urls import path

from .import views

urlpatterns  = [
    path('',views.Index,name='home'),
    path('delete-tracking_history/<id>/', views.delete_transaction,name="delete_transaction"),
    path('login/',views.login_view,name='login'),
    path('register-page/',views.register_page,name='register_page'),
    path('forgotpassowrd-page/',views.forget_password,name='forgetpassword_page'),
]

