# Generated by Django 4.2 on 2023-04-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("department", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="first_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="last_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="patronymic",
            field=models.CharField(max_length=40),
        ),
    ]