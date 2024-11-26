# Generated by Django 4.2.7 on 2024-11-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_user_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseworkTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_tag', to='User.houseworktag'),
        ),
    ]