# Generated by Django 4.0.4 on 2022-04-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0005_alter_incomeaddition_time_alter_incomededuction_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeaddition',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='incomeaddition',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='incomededuction',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='incomededuction',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='tripincome',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tripincome',
            name='time',
            field=models.TimeField(),
        ),
    ]