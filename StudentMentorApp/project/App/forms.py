from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Subject

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username','password1','password2','email','status']
    
    def save(self, commit = True):
        user = super(MyUserForm, self).save(commit=False)
        user.role ="STUDENT"
        user.save()
        return user

class AddSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['ime', 'kod', 'program', 'bodovi', 'sem_redovni', 'sem_izvanredni', 'izborni']
