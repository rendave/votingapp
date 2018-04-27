# Generated by Django 2.0 on 2018-04-27 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0002_auto_20180426_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='votingapp.Party'),
        ),
    ]