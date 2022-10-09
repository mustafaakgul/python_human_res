# Generated by Django 4.1.2 on 2022-10-09 10:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("job", "0009_remove_job_applicant"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="tags_related",
            field=models.ManyToManyField(
                blank=True,
                related_name="tags",
                to=settings.AUTH_USER_MODEL,
                verbose_name="tags_related",
            ),
        ),
    ]