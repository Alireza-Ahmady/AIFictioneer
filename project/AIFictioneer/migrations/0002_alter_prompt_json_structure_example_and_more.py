# Generated by Django 5.0 on 2024-02-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIFictioneer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='json_structure_example',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='name',
            field=models.TextField(),
        ),
    ]
