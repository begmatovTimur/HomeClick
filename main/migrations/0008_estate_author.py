# Generated by Django 4.0.3 on 2022-06-29 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
    ]
