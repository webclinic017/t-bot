# Generated by Django 4.0.4 on 2022-05-27 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('t_bot', '0002_bot_data_created_tbot_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot_data',
            name='bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bot', to='t_bot.tbot'),
        ),
    ]
