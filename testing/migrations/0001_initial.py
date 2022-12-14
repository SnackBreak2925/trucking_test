# Generated by Django 4.1 on 2022-09-02 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('inn_document', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('bio', models.CharField(blank=True, max_length=240)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=10, unique=True)),
                ('from_organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='testing.counterparty')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testing.profile')),
                ('to_organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='testing.counterparty')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=7)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('name', models.CharField(max_length=200)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=7)),
                ('place_quantity', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testing.order')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
