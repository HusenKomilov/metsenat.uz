# Generated by Django 4.2.7 on 2024-05-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsor", "0004_sponsor_default_sum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="default_sum",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1 000 000", "One"),
                    ("5 000 000", "Five"),
                    ("7 000 000", "Seven"),
                    ("10 000 000", "Ten"),
                    ("30 000 000", "Thirty"),
                ],
                max_length=32,
                null=True,
            ),
        ),
    ]
