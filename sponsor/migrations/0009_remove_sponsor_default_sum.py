# Generated by Django 4.2.7 on 2024-05-15 08:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sponsor", "0008_alter_sponsor_organization"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sponsor",
            name="default_sum",
        ),
    ]