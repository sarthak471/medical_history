# Generated by Django 4.1.7 on 2023-04-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_medical_profile', '0007_report_keyword_alter_report_doctors_phoneno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='prescription_img',
            field=models.ImageField(null=True, upload_to='prescription_images/'),
        ),
    ]
