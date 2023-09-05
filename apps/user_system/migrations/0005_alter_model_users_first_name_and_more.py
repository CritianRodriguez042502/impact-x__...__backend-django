# Generated by Django 4.2.4 on 2023-09-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_system', '0004_alter_model_users_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_users',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='model_users',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='model_users',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
