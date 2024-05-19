from django.db import models
from utils.models import BaseModel
from sponsor import choices


class Organization(BaseModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class University(BaseModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class Sponsor(BaseModel):
    full_name = models.CharField(max_length=256, unique=True)
    phone_number = models.CharField(max_length=32, unique=True)

    sponsor_type = models.CharField(max_length=32, choices=choices.SponsorType.choices)  # Jismoniy, Yuridik
    sponsor_condition = models.CharField(max_length=32,
                                         choices=choices.SponsorCondition.choices)  # Yangi, Bekor qilingan
    transfers = models.CharField(max_length=32, choices=choices.SponsorPaymentType.choices)  # Pul o'tkazmalari
    organization = models.CharField(max_length=256, unique=True, blank=True, null=True)

    sponsor_sum = models.IntegerField(default=0)
    separated = models.IntegerField(default=0)  # ajratilgan summa

    def sponsor_separated(self):  # Qolgan summa
        return self.sponsor_sum - self.separated

    def __str__(self):
        return self.full_name


class Student(BaseModel):
    full_name = models.CharField(max_length=128, unique=True)
    phone_number = models.CharField(max_length=32, unique=True)

    student_type = models.CharField(max_length=64, choices=choices.StudentType.choices)

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="university")

    contract = models.IntegerField(default=0)  # kontrakt summasi
    separated = models.IntegerField(default=0, editable=False, blank=True, null=True)  # ajratilgan summa

    is_active = models.BooleanField(default=True)

    def separated_sum(self):  # To'lanishi kerak
        return self.contract - self.separated

    def __str__(self):
        return self.full_name


class StudentSponsor(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    sponsor = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="sponsor")

    separated = models.DecimalField(max_digits=78, decimal_places=0, null=True)  # Ajratilingan summa

    def __str__(self):
        return self.student.full_name
