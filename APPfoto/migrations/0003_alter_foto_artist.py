# Generated by Django 4.2.4 on 2023-09-03 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APPfoto', '0002_remove_foto_artist_name_foto_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
