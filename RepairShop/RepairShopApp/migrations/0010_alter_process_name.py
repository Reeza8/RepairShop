# Generated by Django 4.2.4 on 2023-09-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepairShopApp', '0009_alter_process_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')], max_length=10),
        ),
    ]
