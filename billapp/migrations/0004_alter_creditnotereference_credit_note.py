# Generated by Django 5.0 on 2024-03-16 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0003_auto_20240313_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditnotereference',
            name='credit_note',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='billapp.creditnote'),
        ),
    ]
