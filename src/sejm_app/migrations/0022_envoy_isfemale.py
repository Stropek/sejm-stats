# Generated by Django 5.0 on 2024-04-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sejm_app", "0021_alter_printmodel_options_alter_club_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="envoy",
            name="isFemale",
            field=models.BooleanField(
                blank=True, help_text="Whether the envoy is female", null=True
            ),
        ),
    ]
