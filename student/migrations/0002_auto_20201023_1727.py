# Generated by Django 3.1 on 2020-10-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresponse',
            name='student_response_text',
            field=models.TextField(blank=True, verbose_name='answer here'),
        ),
    ]