# Generated by Django 4.0.6 on 2023-01-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_telawat_arruracy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telawat',
            name='arruracy',
            field=models.CharField(default='Pending', max_length=200),
        ),
    ]
