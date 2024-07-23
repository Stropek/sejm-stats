# Generated by Django 5.0 on 2024-05-06 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sejm_app", "0023_alter_voting_options_alter_voting_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="process",
            name="printModel",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="process",
                to="sejm_app.printmodel",
            ),
        ),
    ]
