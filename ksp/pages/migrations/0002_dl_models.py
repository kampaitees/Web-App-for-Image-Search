# Generated by Django 2.2.2 on 2019-07-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DL_Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facenet_models', models.BinaryField()),
            ],
        ),
    ]