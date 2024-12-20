# Generated by Django 5.1.3 on 2024-11-20 16:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'element',
                'verbose_name_plural': 'elements',
            },
        ),
        migrations.CreateModel(
            name='Type2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'effect',
                'verbose_name_plural': 'effects',
            },
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monsters.type1', verbose_name='element'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monsters.type2', verbose_name='effect'),
        ),
    ]
