# Generated by Django 5.0.1 on 2024-04-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_team_member2_remove_team_member3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round1',
            name='github_link1',
        ),
        migrations.RemoveField(
            model_name='round1',
            name='youtube_link1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='feedback_overall',
        ),
        migrations.AddField(
            model_name='judge',
            name='mode',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='round2',
            name='member2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round2',
            name='member3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round2',
            name='member4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round3',
            name='member2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round3',
            name='member3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round3',
            name='member4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='universalsettings',
            name='upload',
            field=models.BooleanField(default=False),
        ),
    ]
