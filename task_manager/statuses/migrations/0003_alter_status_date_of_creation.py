# Generated by Django 4.2.3 on 2023-07-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_alter_status_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_creation'),
        ),
    ]
