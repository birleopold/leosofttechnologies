# Generated by Django 3.0.5 on 2020-10-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('lan_ports', models.IntegerField(blank=True, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='accessories/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='accessories/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='accessories/')),
                ('imahe4', models.ImageField(blank=True, null=True, upload_to='accessories/')),
            ],
        ),
        migrations.DeleteModel(
            name='Accessory',
        ),
    ]
