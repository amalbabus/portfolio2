# Generated by Django 2.2.13 on 2020-07-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]