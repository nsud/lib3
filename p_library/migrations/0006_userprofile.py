# Generated by Django 2.2.6 on 2020-09-16 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('p_library', '0005_book_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Страна')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='Город')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
    ]
