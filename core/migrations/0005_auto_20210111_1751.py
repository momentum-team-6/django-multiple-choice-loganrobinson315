# Generated by Django 3.1.5 on 2021-01-11 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210111_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.card'),
        ),
    ]
