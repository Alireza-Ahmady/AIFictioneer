# Generated by Django 5.0 on 2024-05-12 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AIFictioneer', '0010_rename_narrative_coherence_structure_ontology_coherence_analysis_output_structure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ontology',
            old_name='narrative_structure_details',
            new_name='ontology_description',
        ),
    ]
