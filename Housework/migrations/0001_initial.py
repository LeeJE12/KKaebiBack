# Generated by Django 4.2.7 on 2024-11-21 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseworkTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('houseworkId', models.AutoField(primary_key=True, serialize=False)),
                ('houseworkDate', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('houseworkPlace', models.CharField(max_length=100, null=True)),
                ('houseworkDetail', models.CharField(max_length=100, null=True)),
                ('houseworkDone', models.BooleanField(default=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_housework', to='Housework.houseworktag')),
            ],
        ),
    ]
