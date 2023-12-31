# Generated by Django 4.1.1 on 2023-01-22 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='user_info',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
