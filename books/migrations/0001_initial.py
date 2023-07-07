# Generated by Django 4.2.2 on 2023-07-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=55, unique=True)),
                ("category", models.CharField(max_length=20)),
                ("author", models.CharField(max_length=55)),
                ("pages", models.IntegerField()),
                ("synopsis", models.TextField()),
                ("avaiable_copies", models.IntegerField(null=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
