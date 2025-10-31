from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TrackerApp

def SaveExpenses(request):
    if request.method == 'POST':
        expenses = request.POST.get('expenses')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        note = request.POST.get('note')

        if not (expenses and amount and category and note):
            messages.error(request, "Please fill all fields before submission.")
        else:
            TrackerApp.objects.create(
                expenses=expenses,
                amount=amount,
                category=category,
                note=note
            )
            messages.success(request, "Expense saved successfully!")

        return redirect('save') 
    
    all_expenses = TrackerApp.objects.all().order_by('-date_registered')
    return render(request, 'frontend/index.html', {'expenses_list': all_expenses})


def delete_expense(request, id):
    expense = TrackerApp.objects.get(id=id)
    expense.delete()
    messages.success(request, "Expense deleted successfully!")
    return redirect('save')
