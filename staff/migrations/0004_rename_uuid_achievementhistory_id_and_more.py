# Generated by Django 4.2.7 on 2023-11-21 06:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0003_remove_userproject_current_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="achievementhistory",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="designation",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="grievance",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="promotionhistory",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="servicerecord",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="tasklog",
            old_name="uuid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="userproject",
            old_name="uuid",
            new_name="id",
        ),
    ]
