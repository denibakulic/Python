from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class MyUser(AbstractUser):
    class Role(models.TextChoices):
        MENTOR = "MENTOR", _('mentor')
        STUDENT = "STUDENT", _('student')

    role = models.CharField(choices=Role.choices, default=Role.STUDENT, max_length=64)

    class Status(models.TextChoices):
        NONE = "NONE", _('none')
        REDOVNI = "REDOVNI", _('redovni')
        IZVANREDNI = "IZVANREDNI", _('izvanredni')

    status = models.CharField(choices=Status.choices, default=Status.NONE, max_length=64)

class Subject(models.Model):
    ime = models.CharField(max_length=255)
    kod = models.CharField(max_length=16, unique=True)
    program = models.TextField()
    bodovi = models.IntegerField()
    sem_redovni = models.IntegerField()
    sem_izvanredni = models.IntegerField()

    class Izborni(models.TextChoices):
        DA = "DA", _('Da')
        NE = "NE", _('Ne')

    izborni = models.CharField(choices=Izborni.choices, default=Izborni.NE, max_length=2)

    def __str__(self):
        return '%s - %s' % (self.kod, self.ime)

class Enrolment(models.Model):
    
    student_id = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    predmet_id = models.ForeignKey('Subject', on_delete=models.CASCADE)
    status = models.CharField(max_length=64)

    def __str__(self):
        return '%s - %s - %s' % (self.student_id, self.predmet_id, self.status)