from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser, Subject, Enrolment
from .forms import MyUserForm, AddSubjectForm
from django.contrib import messages
from .decorations import mentor_required, student_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# User managemenet


def register_view(request):
    if request.method == 'GET':
        userForm = MyUserForm()
        return render(request, 'register.html', {'form':userForm})
    elif request.method == 'POST':
        userForm = MyUserForm(request.POST)
        if userForm.is_valid():
            user = userForm.cleaned_data.get('username')
            messages.success(request, f'Acount created for {user}!')
            userForm.save()
            return redirect ('login')
        else:
            return render(request, 'register.html', {'form':userForm})
    else:
        return HttpResponseNotAllowed()

# @login_required
def login_view(request):
    if request.method == 'GET':
        userForm = AuthenticationForm()
        return render(request, 'login.html', {'form':userForm})
    elif request.method == 'POST':
        userForm = AuthenticationForm(data=request.POST)
        if userForm.is_valid() and userForm is not None:
            user = userForm.get_user()
            if user.role == 'MENTOR': 
                login(request, user)
                return redirect('student_list')
            login(request,user)
            return redirect('enrolment')
    else:
        return HttpResponseNotAllowed()

def logout_view(request):
    return render (request,'logout.html')

#######

#Upisni list (student)

def enroll(subject_id, student):
    if not Enrolment.objects.filter(student_id_id=student.id, predmet_id_id=subject_id):
        Enrolment.objects.create(student_id_id=student.id, predmet_id_id=subject_id, status='enrolled')

def delete(subject_id, student):
    Enrolment.objects.filter(predmet_id_id=subject_id, student_id_id=student.id).delete()

def passed(subject_id, student):
    Enrolment.objects.filter(predmet_id_id=subject_id, student_id_id=student.id).update(status='passed')

def not_passed(subject_id, student):
    Enrolment.objects.filter(predmet_id_id=subject_id, student_id_id=student.id).delete()

@student_required
def enrolment_view(request):
    if (request.user.is_authenticated):
        username = request.user.get_username()
        student = MyUser.objects.get(username=username)
        if(request.method == 'POST'):
            if request.POST.get('upisi'):
                enroll(request.POST.get('upisi'),student)
            elif request.POST.get('delete'):
                delete(request.POST.get('delete'),student)
            elif request.POST.get('passed'):
                passed(request.POST.get('passed'),student)
            elif request.POST.get('not_passed'):
                not_passed(request.POST.get('not_passed'),student)
    
        enrolled = Enrolment.objects.filter(student_id_id=student.id).order_by('predmet_id')
        subjects = Subject.objects.exclude(id__in=enrolled.values('predmet_id'))
        subj_all = Subject.objects.all()
        if student.status == 'REDOVNI':
            br_sem = 6
        else:
            br_sem = 8
        context = {
            'subjects':subjects,
            'enrolled':enrolled,
            'student':student,
            'semestar':range(1, br_sem + 1),
            'all':subj_all
        }
        return render(request, 'enrolment.html', context)
    else:
        return redirect ('login')

######

#(mentor)

@mentor_required
def subject_list_view(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        return render (request, 'subject_list.html',{'subjects':subjects})
    elif request.method == 'POST':
        if request.POST.get("delete"):
            delete = request.POST.get("delete")
            Subject.objects.filter(id=delete).delete()
            return redirect('subject_list')


@mentor_required
def add_subject_view(request):
    if request.method == 'GET':
        newsubj = AddSubjectForm()
        return render(request, 'add_subject.html', {'subform':newsubj})
    elif request.method == 'POST':
        newsubj = AddSubjectForm(request.POST)
        if newsubj.is_valid():
            newsubj.save()
            return redirect('subject_list')
        else:
            return render (request, 'add_subject.html', {'subform':newsubj})

@mentor_required
def subject_details_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    return render(request, 'subj_details.html', {'subject':subject})

@mentor_required
def edit_subject_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'GET':
        subjectForm = AddSubjectForm()
        subjectForm.fields['ime'].initial = subject.ime
        subjectForm.fields['kod'].initial = subject.kod
        subjectForm.fields['program'].initial = subject.program
        subjectForm.fields['bodovi'].initial = subject.bodovi
        subjectForm.fields['sem_redovni'].initial = subject.sem_redovni
        subjectForm.fields['sem_izvanredni'].initial = subject.sem_izvanredni
        subjectForm.fields['izborni'].initial = subject.izborni
        return render(request, 'edit_subj.html', {'subform':subjectForm})
    elif request.method == 'POST':
        subjectForm = AddSubjectForm(request.POST, instance=subject)
        if subjectForm.is_valid():
            subjectForm.save()
            return redirect('subject_list')
        else:
            return render(request, 'edit_subj.html', {'subform':subjectForm})

@mentor_required
def student_list_view(request):
    students = MyUser.objects.filter(role='STUDENT')
    return render (request, 'student_list.html', {'students':students})

#upisni list (mentor)

def mentor_enrolment_view(request, student_id):
    student = MyUser.objects.get(id=student_id)
    print(student)
    if(request.method == 'POST'):
        if request.POST.get('upisi'):
            enroll(request.POST.get('upisi'),student)
        elif request.POST.get('delete'):
            delete(request.POST.get('delete'),student)
        elif request.POST.get('passed'):
            passed(request.POST.get('passed'),student)
        elif request.POST.get('not_passed'):
                not_passed(request.POST.get('not_passed'),student)

    enrolled = Enrolment.objects.filter(student_id_id=student.id).order_by('predmet_id')
    subjects = Subject.objects.exclude(id__in=enrolled.values('predmet_id'))
    subj_all = Subject.objects.all()
    if student.status == 'REDOVNI':
        br_sem = 6
    else:
        br_sem = 8
    context = {
        'subjects':subjects,
        'enrolled':enrolled,
        'student':student,
        'semestar':range(1, br_sem + 1),
        'all':subj_all
    }
    return render(request, 'enrolment.html', context)