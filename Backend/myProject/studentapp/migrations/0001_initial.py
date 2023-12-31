# Generated by Django 4.2.4 on 2023-09-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=50)),
                ('studentId', models.CharField(max_length=30, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('date_of_Birth', models.DateField()),
                ('major', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Business', 'Business')], max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
    ]
