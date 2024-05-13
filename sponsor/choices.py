from django.db import models


class SponsorSum(models.TextChoices):
    ONE = "1 000 000"
    FIVE = "5 000 000"
    SEVEN = "7 000 000"
    TEN = "10 000 000"
    THIRTY = "30 000 000"


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
