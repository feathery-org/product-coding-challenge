# Generated by Django 5.0.7 on 2024-07-27 03:48

import uuid
from django.db import migrations, models

def seed_mymodel(apps, schema_editor):
    Field = apps.get_model('form', 'Field')
    
    data = [
        {'option': 'text_field'},
        {'option': 'dropdown_field'},
        {'option': 'checkbox_field'},
    ]
    
    for entry in data:
        Field.objects.get_or_create(**entry)
        
class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_form_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('option', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.RunPython(seed_mymodel),
    ]
