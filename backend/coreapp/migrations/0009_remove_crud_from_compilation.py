# Generated by Django 3.2.4 on 2021-11-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0008_scratch_max_score_squashed_0011_alter_scratch_compiler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compilation',
            name='elf_object',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='stderr',
        ),
        migrations.RemoveField(
            model_name='compilation',
            name='hash',
        ),
        migrations.AddField(
            model_name='compilation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
