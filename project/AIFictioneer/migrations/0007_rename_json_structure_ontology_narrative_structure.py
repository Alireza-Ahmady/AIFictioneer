# Generated by Django 5.0 on 2024-04-02 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AIFictioneer', '0006_ontology_ttl_definition_alter_ontology_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ontology',
            old_name='json_structure',
            new_name='narrative_structure',
        ),
    ]