# Generated by Django 3.0.5 on 2020-05-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200503_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]