# Generated by Django 3.0.6 on 2020-07-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]
