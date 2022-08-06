# Generated by Django 3.2.8 on 2021-12-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NormalUser', '0009_auto_20211111_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaldeclaration',
            name='departure_city',
        ),
        migrations.RemoveField(
            model_name='medicaldeclaration',
            name='departure_detailed_place',
        ),
        migrations.RemoveField(
            model_name='medicaldeclaration',
            name='departure_province',
        ),
        migrations.RemoveField(
            model_name='medicaldeclaration',
            name='departure_ward',
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='gender',
            field=models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ'), ('O', 'Khác')], max_length=1),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
