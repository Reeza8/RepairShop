# Generated by Django 4.2.4 on 2023-08-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepairShopApp', '0002_alter_process_exit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='exit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]