# Generated by Django 4.1.5 on 2023-01-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_pontoturistico_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]