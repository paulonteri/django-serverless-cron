# Generated by Django 3.2.11 on 2022-01-27 11:12

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobRun',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('function_path', models.CharField(help_text='The path to the function executed.', max_length=255)),
                ('kwargs', models.JSONField(blank=True, help_text='The kwargs to passed to the function.', null=True)),
                ('frequency', models.CharField(blank=True, help_text='The frequency that was set for the job.', max_length=255, null=True)),
                ('time_attempted_running', models.DateTimeField(default=django.utils.timezone.now, help_text='Time when first attempted to run the job')),
                ('time_finished_running', models.DateTimeField(blank=True, help_text='Time when the job finished running', null=True)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-time_attempted_running',),
            },
        ),
    ]
