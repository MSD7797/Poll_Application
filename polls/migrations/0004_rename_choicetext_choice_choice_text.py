# Generated by Django 4.0.5 on 2022-06-16 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_choice_text_choice_choicetext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choicetext',
            new_name='choice_text',
        ),
    ]
