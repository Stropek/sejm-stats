# Generated by Django 5.0 on 2024-10-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sejm_app", "0025_alter_printmodel_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="process",
            name="createdBy",
            field=models.CharField(
                blank=True,
                choices=[
                    ("posłowie", "Envoys"),
                    ("klub", "Club"),
                    ("prezydium", "Presidium"),
                    ("obywatele", "Citizens"),
                    ("rząd", "Government"),
                ],
                default="Brak danych",
                max_length=20,
                null=True,
            ),
        ),
    ]
