# Generated by Django 5.0.1 on 2024-01-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vazifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('tavsif', models.TextField(null=True)),
                ('oxirgi_muddat', models.DateField()),
            ],
            options={
                'verbose_name': 'Vazifa',
                'verbose_name_plural': 'Vazifalar',
            },
        ),
    ]