# Generated by Django 5.0.3 on 2024-04-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_mcqquestion_mcqchoice_quiz_mcqquestion_quiz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='pointsperquestion',
            field=models.IntegerField(default=1),
        ),
    ]
