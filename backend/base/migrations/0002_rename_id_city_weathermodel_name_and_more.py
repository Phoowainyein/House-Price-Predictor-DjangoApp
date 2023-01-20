# Generated by Django 4.1.5 on 2023-01-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weathermodel',
            old_name='id_city',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='weathermodel',
            old_name='temperature',
            new_name='temperature_neg',
        ),
        migrations.AddField(
            model_name='weathermodel',
            name='temperature_curr',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='weathermodel',
            name='temperature_pos',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=50, null=True),
        ),
    ]