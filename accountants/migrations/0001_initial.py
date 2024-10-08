# Generated by Django 5.0.6 on 2024-08-14 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=45, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='FiscalYears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=45)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('role', models.CharField(choices=[('accountant', 'accountant'), ('manager', 'manager')], max_length=45)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('identifier', models.CharField(max_length=256)),
                ('notes', models.TextField()),
                ('amount', models.PositiveSmallIntegerField()),
                ('suspended', models.BooleanField(default=False)),
                ('suspend_reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountants.countries')),
            ],
            options={
                'db_table': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Transcations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('debtor', 'debtor'), ('creditors', 'creditors')], max_length=45)),
                ('transcation_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveSmallIntegerField()),
                ('notres', models.TextField()),
                ('fiscal_year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accountants.fiscalyears')),
                ('owner_person', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accountants.persons')),
                ('commited_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accountants.users')),
                ('reviewed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='reviewer', to='accountants.users')),
            ],
            options={
                'db_table': 'transcations',
            },
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=10, max_digits=19)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accountants.users')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
