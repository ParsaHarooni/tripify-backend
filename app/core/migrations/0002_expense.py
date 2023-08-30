# Generated by Django 4.2.3 on 2023-08-30 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=128, verbose_name='reason')),
                ('price', models.IntegerField(max_length=128, verbose_name='price')),
                ('category', models.CharField(choices=[('SH', 'Shopping'), ('F', 'Food'), ('C', 'Commute'), ('E', 'Entertainment'), ('O', 'Other')], max_length=2, verbose_name='category')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trip', verbose_name='trip')),
            ],
        ),
    ]
