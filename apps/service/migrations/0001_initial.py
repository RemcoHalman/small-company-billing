# Generated by Django 4.0 on 2022-01-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, help_text='Service description max length 150 characters', max_length=150, null=True)),
                ('price_per_hour', models.DecimalField(decimal_places=2, default=42.5, help_text='Default has been set to €42,50', max_digits=4)),
                ('hours', models.TimeField(default='1:00', help_text='Time spend for doing the service')),
                ('tax_value', models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='service_tax', to='common.tax')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, help_text='Product description max length 150 characters', max_length=150, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=10.0, help_text='Price per product, price without TAX. This will be automatically added', max_digits=4)),
                ('tax_value', models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='product_tax', to='common.tax')),
            ],
        ),
    ]
