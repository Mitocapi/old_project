# Generated by Django 4.2.4 on 2023-09-03 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APPfoto', '0003_alter_foto_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='artist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
