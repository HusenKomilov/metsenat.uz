from django.db import models


class SponsorType(models.TextChoices):
    PYSICAL = "Jismoniy shaxs"
    LEGAL = "Yuridik shaxs"


class SponsorCondition(models.TextChoices):
    NEW = "Yangi"
    MODERNIZATION = "Modernizatsiyada"
    CHECK = "Tasdiqlangan"
    CANCELED = "Bekor qilingan"


class SponsorPaymentType(models.TextChoices):
    MONEY_TRANSFERS = "Pul o'tkazmalari"


class StudentType(models.TextChoices):
    BACHELOR = "Bakalavr"
    MASTER = "Magister"
