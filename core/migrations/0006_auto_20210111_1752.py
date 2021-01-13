# Generated by Django 3.1.5 on 2021-01-11 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210111_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='card',
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.deck'),
        ),
    ]