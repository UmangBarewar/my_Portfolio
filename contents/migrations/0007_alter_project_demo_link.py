# Generated by Django 5.0.7 on 2024-07-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_alter_profile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
