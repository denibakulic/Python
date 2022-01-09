"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import register_view, student_list_view, subject_list_view,add_subject_view, login_view, logout_view, enrolment_view, subject_details_view, edit_subject_view, mentor_enrolment_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('stud_list/', student_list_view, name='student_list'),
    path('sub_list/', subject_list_view, name='subject_list'),
    path('addsubj/', add_subject_view, name='add_subject'),
    path('enrolment/', enrolment_view, name='enrolment'),
    path('enrolment/<int:student_id>', mentor_enrolment_view, name='enrolment'),
    path('subj_details/<int:subject_id>', subject_details_view, name='subject_details'),
    path('edit_subj/<int:subject_id>', edit_subject_view, name='edit_subject'),
]
