# Generated by Django 4.1.7 on 2023-04-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newtitle', models.CharField(max_length=15, verbose_name='Название вести')),
                ('newdesc', models.TextField(verbose_name='Описание вести')),
            ],
        ),
    ]
