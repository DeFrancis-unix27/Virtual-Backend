# Generated manually for Gallery model

from django.db import migrations, models
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_testimonails_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
