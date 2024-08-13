# Generated by Django 5.0 on 2024-08-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.JSONField()),
                ("image", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "role",
                    models.IntegerField(
                        choices=[
                            (0, "Twórca aplikacji"),
                            (1, "Programista"),
                            (2, "Wyjątkowo chojny wspierający"),
                            (3, "Wspierający"),
                        ],
                        default=3,
                    ),
                ),
                ("since", models.CharField(default="YYYY-MM", max_length=7)),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("about", models.TextField(blank=True, null=True)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="photos")),
            ],
            options={
                "ordering": ["-role"],
            },
        ),
    ]
