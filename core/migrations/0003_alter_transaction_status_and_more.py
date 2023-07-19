# Generated by Django 4.2.3 on 2023-07-18 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_transaction_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('failed', 'failed'), ('completed', 'completed'), ('pending', 'pending'), ('processing', 'processing'), ('request_sent', 'request_sent'), ('request_settled', 'request_settled'), ('request_processing', 'request_processing')], default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('transfer', 'Transfer'), ('received', 'Received'), ('withdraw', 'Withdraw'), ('refund', 'Refund'), ('request', 'Payment Request'), ('none', 'None')], default='none', max_length=100),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=20, prefix='CARD', unique=True)),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('card_type', models.CharField(choices=[('master', 'master'), ('visa', 'visa'), ('verve', 'verve')], default='master', max_length=20)),
                ('card_status', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
