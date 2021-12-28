# Generated by Django 4.0 on 2021-12-28 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer_type', models.CharField(choices=[('Individual', 'Individual'), ('Business', 'Business')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IBAN_number', models.CharField(blank=True, help_text='Bank account number', max_length=25, null=True)),
                ('vat_number', models.CharField(blank=True, help_text='VAT number / BTW nummer', max_length=25, null=True)),
                ('register_number', models.CharField(blank=True, help_text='Chamber of Commerce / KVK nummer', max_length=64, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=64)),
                ('address_line_2', models.CharField(blank=True, max_length=64, null=True)),
                ('house_number', models.IntegerField()),
                ('appartment_addition', models.CharField(blank=True, max_length=64, null=True)),
                ('zip_code', models.CharField(max_length=6)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='billing.country')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
            ],
        ),
    ]
