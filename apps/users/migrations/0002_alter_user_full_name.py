# Generated by Django 5.0.7 on 2024-07-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Abror Nematjanov', max_length=250, verbose_name='Full Name'),
            preserve_default=False,
        ),
    ]
