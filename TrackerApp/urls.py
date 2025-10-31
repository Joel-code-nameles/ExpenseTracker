from django.urls import path
from . import views

urlpatterns = [
    path('', views.SaveExpenses, name='save'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
]
