# Generated by Django 5.2.4 on 2025-07-06 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityGuard',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.user')),
                ('guardID', models.IntegerField(unique=True)),
                ('guardemail', models.EmailField(max_length=254, unique=True)),
                ('guardname', models.CharField(max_length=100)),
            ],
            bases=('myapp.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.user')),
                ('studentID', models.IntegerField(unique=True)),
                ('studentemail', models.EmailField(max_length=254, unique=True)),
                ('studentname', models.CharField(max_length=100)),
            ],
            bases=('myapp.user',),
        ),
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=100)),
                ('itemDescription', models.TextField()),
                ('itemImage', models.ImageField(upload_to='lost_items/')),
                ('lostDate', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=100)),
                ('itemDescription', models.TextField()),
                ('itemImage', models.ImageField(upload_to='found_items/')),
                ('foundDate', models.DateField()),
                ('guardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]
