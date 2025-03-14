# Generated by Django 5.0 on 2025-01-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='requires_prescription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dosage_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='side_effects',
        ),
        migrations.AddField(
            model_name='product',
            name='skin_type',
            field=models.CharField(choices=[('all', 'All Skin Types'), ('oily', 'Oily Skin'), ('dry', 'Dry Skin'), ('combination', 'Combination Skin'), ('sensitive', 'Sensitive Skin')], default='all', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='skin_concern',
            field=models.CharField(choices=[('acne', 'Acne Treatment'), ('aging', 'Anti-Aging'), ('brightening', 'Brightening'), ('hydration', 'Hydration'), ('sun_protection', 'Sun Protection')], default='hydration', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='how_to_use',
            field=models.TextField(blank=True),
        ),
    ]
