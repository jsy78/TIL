

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Received_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_username', models.CharField(max_length=30)),
                ('received_username', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('is_important', models.BooleanField(default=False)),
                ('is_trash', models.BooleanField(default=False)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('received_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sent_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_username', models.CharField(max_length=30)),
                ('received_username', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('received_note', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.received_note')),
                ('sent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
