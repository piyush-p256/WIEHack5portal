# Generated by Django 5.0.1 on 2024-04-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_judge'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='judge_name',
            field=models.CharField(default='judge1', max_length=255),
        ),
    ]
