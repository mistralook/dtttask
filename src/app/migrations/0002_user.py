# Generated by Django 4.0.2 on 2022-02-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("username", models.CharField(max_length=32)),
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("phone", models.CharField(max_length=16)),
            ],
        ),
    ]