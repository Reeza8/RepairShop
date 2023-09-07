# Generated by Django 4.2.4 on 2023-09-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepairShopApp', '0006_alter_process_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(choices=[('1', 'process1'), ('2', 'process2'), ('3', 'process3'), ('4', 'process4'), ('5', 'process5')], max_length=10),
        ),
    ]