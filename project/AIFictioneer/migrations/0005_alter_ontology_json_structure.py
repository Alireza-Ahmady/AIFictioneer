# Generated by Django 5.0 on 2024-03-11 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIFictioneer', '0004_alter_ontology_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ontology',
            name='json_structure',
            field=models.TextField(blank=True, null=True),
        ),
    ]
