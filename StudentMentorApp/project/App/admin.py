from django.contrib import admin

# Register your models here.

from .models import MyUser, Subject, Enrolment
from .forms import MyUserForm
# from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser)
admin.site.register(Subject)
admin.site.register(Enrolment)