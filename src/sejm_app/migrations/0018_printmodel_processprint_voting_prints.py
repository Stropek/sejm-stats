# Generated by Django 5.0 on 2024-04-19 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sejm_app", "0017_alter_vote_vote"),
    ]

    operations = [
        migrations.AddField(
            model_name="printmodel",
            name="processPrint",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="sejm_app.printmodel",
            ),
        ),
        migrations.AddField(
            model_name="voting",
            name="prints",
            field=models.ManyToManyField(
                blank=True,
                help_text="Prints related to the voting",
                related_name="votings",
                to="sejm_app.printmodel",
            ),
        ),
    ]
