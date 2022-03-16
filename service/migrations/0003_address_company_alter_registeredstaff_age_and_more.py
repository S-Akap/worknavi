# Generated by Django 4.0.2 on 2022-03-16 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_registeredstaff_citizenship_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(blank=True, max_length=8, verbose_name='郵便番号')),
                ('address1', models.CharField(blank=True, max_length=40, verbose_name='都道府県')),
                ('address2', models.CharField(blank=True, max_length=40, verbose_name='市区町村番地')),
                ('address3', models.CharField(blank=True, max_length=40, verbose_name='建物名')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='会社名')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.address', verbose_name='会社住所')),
            ],
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='age',
            field=models.IntegerField(verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='citizenship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='service.citizenship', verbose_name='国籍'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='hourly_pay',
            field=models.IntegerField(blank=True, null=True, verbose_name='希望時給'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='is_contact',
            field=models.BooleanField(verbose_name='連絡がすぐ繋がるか'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='service.requirement', verbose_name='資格'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='residence',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='居住地'),
        ),
        migrations.AlterField(
            model_name='registeredstaff',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.sex', verbose_name='性別'),
        ),
        migrations.CreateModel(
            name='RegisteredCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('hourly_pay', models.IntegerField(blank=True, null=True, verbose_name='希望時給')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('citizenship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='service.citizenship', verbose_name='国籍')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.company', verbose_name='求人会社')),
                ('requirement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='service.requirement', verbose_name='資格')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.sex', verbose_name='性別')),
            ],
        ),
    ]