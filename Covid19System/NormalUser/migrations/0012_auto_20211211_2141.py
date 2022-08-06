# Generated by Django 3.2.8 on 2021-12-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NormalUser', '0011_auto_20211211_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaldeclaration',
            name='in_contact_confirmed_COVID19_case',
            field=models.CharField(choices=[('Có', 'Không'), ('Có', 'Không')], max_length=6),
        ),
        migrations.AlterField(
            model_name='medicaldeclaration',
            name='in_contact_people_from_countries_with_COVID19',
            field=models.CharField(choices=[('Có', 'Không'), ('Có', 'Không')], max_length=6),
        ),
        migrations.AlterField(
            model_name='medicaldeclaration',
            name='in_contact_people_with_syptoms',
            field=models.CharField(choices=[('Có', 'Không'), ('Có', 'Không')], max_length=6),
        ),
        migrations.AlterField(
            model_name='medicaldeclaration',
            name='past_14d_symptoms',
            field=models.CharField(choices=[('Có', 'Không'), ('Có', 'Không')], max_length=6),
        ),
        migrations.AlterField(
            model_name='medicaldeclaration',
            name='past_14d_travel',
            field=models.CharField(choices=[('Có', 'Không'), ('Có', 'Không')], max_length=6),
        ),
    ]
