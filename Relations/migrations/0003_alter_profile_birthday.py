# Generated by Django 4.0.1 on 2022-01-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relations', '0002_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(default='2000-02-21'),
            preserve_default=False,
        ),
    ]
