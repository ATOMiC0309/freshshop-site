# Generated by Django 5.0.6 on 2024-05-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]