# Generated by Django 5.0.6 on 2024-06-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuarios",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.TextField(max_length=255)),
                ("idade", models.IntegerField()),
            ],
        ),
    ]