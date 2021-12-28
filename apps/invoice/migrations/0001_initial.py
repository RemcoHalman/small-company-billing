# Generated by Django 4.0 on 2021-12-28 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('customer', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_title', models.CharField(max_length=200)),
                ('invoice_number', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice_created_by', to='account.customuser')),
                ('due_date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='common.duedate')),
                ('invoice_state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_state', to='common.invoicestate')),
                ('tax_value', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_tax', to='common.tax')),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_to_address', to='customer.address')),
            ],
        ),
    ]