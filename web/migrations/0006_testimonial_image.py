# Generated by Django 3.2.9 on 2021-11-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='abcd', upload_to='testimonials/'),
            preserve_default=False,
        ),
    ]
