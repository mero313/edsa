# Generated by Django 4.1.7 on 2023-02-23 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.people'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='people',
        ),
        migrations.AlterField(
            model_name='food',
            name='people',
            field=models.ManyToManyField(to='country.people'),
        ),
        migrations.AlterField(
            model_name='people',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='event',
            name='people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.people'),
        ),
    ]
