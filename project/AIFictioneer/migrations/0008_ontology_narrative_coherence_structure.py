# Generated by Django 5.0 on 2024-04-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIFictioneer', '0007_rename_json_structure_ontology_narrative_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='ontology',
            name='narrative_coherence_structure',
            field=models.TextField(blank=True, null=True),
        ),
    ]