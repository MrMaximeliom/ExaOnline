# Generated by Django 3.0.6 on 2020-07-18 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20200715_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_number_of_questions',
            field=models.IntegerField(blank=True, null=True, verbose_name='exam number of questions'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=650)),
                ('question_optimal_answer', models.TextField()),
                ('question_degree', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='teacher.Exam')),
            ],
        ),
    ]
