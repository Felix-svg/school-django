# Generated by Django 5.0.6 on 2024-06-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('teacher', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
                ('students', models.IntegerField()),
            ],
        ),
    ]