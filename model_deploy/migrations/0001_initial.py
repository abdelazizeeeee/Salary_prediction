# Generated by Django 4.2.5 on 2023-11-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('exp', models.CharField(max_length=100)),
                ('educ_lvl', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
            ],
        ),
    ]
