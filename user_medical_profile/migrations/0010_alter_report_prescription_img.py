# Generated by Django 4.1.7 on 2023-04-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_medical_profile', '0009_alter_report_prescription_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='prescription_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]