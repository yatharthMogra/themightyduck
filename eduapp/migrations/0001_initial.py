# Generated by Django 3.1.7 on 2021-02-28 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(default=1, unique=True)),
                ('question_content', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_number', models.IntegerField(default=1)),
                ('option_content', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.questions')),
            ],
        ),
    ]
