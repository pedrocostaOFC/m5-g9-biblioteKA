# Generated by Django 4.2.2 on 2023-07-11 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copies', '0001_initial'),
        ('loans', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='copy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='copies.copy'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(),
        ),
    ]
