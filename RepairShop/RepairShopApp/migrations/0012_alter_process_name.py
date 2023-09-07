# Generated by Django 4.2.4 on 2023-09-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepairShopApp', '0011_alter_process_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.IntegerField(choices=[(0, 'process1'), (1, 'process2'), (2, 'process3'), (3, 'process4'), (4, 'process5')], default=0),
        ),
    ]
