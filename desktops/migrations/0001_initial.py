# Generated by Django 3.0.5 on 2020-10-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='accessories/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='accessories/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='accessories/')),
                ('imahe4', models.ImageField(blank=True, null=True, upload_to='accessories/')),
            ],
        ),
    ]
