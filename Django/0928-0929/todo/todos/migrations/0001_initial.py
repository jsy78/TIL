# Generated by Django 3.2.13 on 2022-09-29 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10)),
                ('completed', models.BooleanField()),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(null=True)),
            ],
        ),
    ]
