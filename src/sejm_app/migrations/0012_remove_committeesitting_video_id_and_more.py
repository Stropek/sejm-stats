# Generated by Django 5.0 on 2024-03-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sejm_app", "0011_alter_committeemember_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="committeesitting",
            name="video_id",
        ),
        migrations.AddField(
            model_name="committeesitting",
            name="video_url",
            field=models.URLField(null=True),
        ),
    ]
