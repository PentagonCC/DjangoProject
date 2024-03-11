from django import forms
from django.contrib.auth import get_user_model

from web.models import Task, Transaction

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password1']:
            self.add_error('password', 'Пароли не совпадают')
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password", "password1")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TaskForm(forms.ModelForm):
    creation_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"},
                                                                   format='%Y-%m-%dT%H:%M'
    ))

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Task
        fields = ('task_name', 'creation_date', 'status', 'task_description')


class TransactionForm(forms.ModelForm):
    transaction_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"},
                                                                   format='%Y-%m-%dT%H:%M'
    ))

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Transaction
        fields = ('amount', 'category', 'transaction_date', 'description')
