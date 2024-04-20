# Generated by Django 5.0.1 on 2024-04-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_remove_round1_ieee_id_remove_round1_ieee_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='member2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='member3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='member4',
        ),
        migrations.AddField(
            model_name='round1',
            name='member2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round1',
            name='member3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='round1',
            name='member4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
