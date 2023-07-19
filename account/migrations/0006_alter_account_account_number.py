# Generated by Django 4.2.3 on 2023-07-13 18:48

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=25, prefix='217', unique=True),
        ),
    ]