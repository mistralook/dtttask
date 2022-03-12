# Generated by Django 4.0.3 on 2022-03-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_user_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]
