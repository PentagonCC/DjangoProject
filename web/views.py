from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from web.forms import RegistrationForm, AuthForm, TaskForm, TransactionForm
from web.models import Task, Transaction

User = get_user_model()


def main_view(request):
    tasks = Task.objects.all()
    return render(request, 'web/example.html', {
        'tasks': tasks
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, 'web/registration.html', {
        'form': form, 'is_success': is_success
    })


def auth_view(request):
    form = AuthForm
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены некорректные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, 'web/auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')


def task_edit_view(request, id =None):
    task = Task.objects.get(id=id) if id is not None else None
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(data=request.POST, instance=task, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, 'web/task_form.html', {'form': form})


def task_delete_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("main")


def transaction_view(request):
    transaction = Transaction.objects.all()
    form = TransactionForm
    return render(request, 'web/transaction.html', {'transaction': transaction, 'form': form})

