# Generated by Django 2.0.7 on 2018-07-13 08:59

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaidName_text', models.CharField(default='', help_text='Please enter the name of the Paid Employee/Firm', max_length=200, verbose_name='Paid Person/Firm')),
                ('TypeOfDocument', models.CharField(choices=[('Fatura', 'Fatura'), ('Fiş', 'Fiş'), ('İrsaliye', 'İrsaliye')], default='Fatura', max_length=9)),
                ('DateOfDocument', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='The date of the Document')),
                ('DocumentID', models.CharField(default='', help_text='Please enter the document ID', max_length=200, verbose_name='Document ID')),
                ('PaymentStatus', models.CharField(choices=[('Paid', 'Yes'), ('Not Paid', 'No')], default='Yes', max_length=9)),
                ('PaymentDate', models.DateField(default=datetime.datetime.now, verbose_name='Date of Payment')),
                ('PaymentSum', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MaxValueValidator(999999999999)], verbose_name='Payment Sum')),
                ('UltraTotalSum', models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MaxValueValidator(999999999999)], verbose_name='Payment Sum')),
                ('Currency', models.CharField(choices=[('TL', 'TL'), ('USD', 'USD'), ('EUR', 'EUR')], default='TL', max_length=9)),
                ('TotalSum', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Total Sum in TL')),
                ('description', models.CharField(blank=True, help_text='Write a brief description', max_length=100, verbose_name='Description of the Customer')),
                ('MethodOfPayment', models.CharField(help_text='Please enter the name of the Payer', max_length=200, verbose_name='Method Of Payment')),
                ('PayingEmployee', models.CharField(help_text='Please enter the name of the Paying Employee', max_length=100, verbose_name='Name of the Paying Employee')),
                ('BooleanPayment', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'ordering': ['DateOfDocument'],
            },
        ),
        migrations.CreateModel(
            name='maincategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainCategoryMember', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryMember', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='SubCategoryExpense',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MoneyRelations.subcategory'),
        ),
        migrations.AddField(
            model_name='expense',
            name='mainCategoryExpense',
            field=models.ForeignKey(default='', help_text='Please start typing.. Sub Category will appear after you select Main Category', max_length=30, on_delete=django.db.models.deletion.CASCADE, to='MoneyRelations.maincategory'),
        ),
    ]
