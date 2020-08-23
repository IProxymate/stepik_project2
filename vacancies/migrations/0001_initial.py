# Generated by Django 3.1 on 2020-08-22 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('location', models.CharField(default='', max_length=120)),
                ('logo', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('employee_count', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=20, unique=True)),
                ('title', models.CharField(default='', max_length=40)),
                ('picture', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('skills', models.TextField(default='')),
                ('description', models.TextField()),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('published_at', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                              to='vacancies.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                                to='vacancies.specialty')),
            ],
        ),
    ]
