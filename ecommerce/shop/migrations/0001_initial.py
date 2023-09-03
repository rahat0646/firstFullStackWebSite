# Generated by Django 4.2.4 on 2023-09-03 16:21

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
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Biz hakda(text):')),
                ('phone', models.PositiveIntegerField(default=0, verbose_name='Telefon belgi(6xxxxxxx):')),
                ('phone2', models.PositiveIntegerField(blank=True, default=0, verbose_name='Telefon belgi2(6xxxxxxx):')),
                ('phone3', models.PositiveIntegerField(blank=True, default=0, verbose_name='Telefon belgi3(6xxxxxxx):')),
                ('email', models.CharField(default='', max_length=50, verbose_name='E-Pocta salgynyz:')),
                ('adress', models.CharField(default='', max_length=100, verbose_name='Yerlesyan yeriniz:')),
                ('image', models.ImageField(upload_to='about_us/', verbose_name='Biz hakda ucin logo:')),
            ],
            options={
                'verbose_name_plural': 'Biz hakda',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Banner ady:')),
                ('image', models.ImageField(upload_to='img/', verbose_name='Banner suraty:')),
                ('link', models.CharField(max_length=1000, verbose_name='Link:')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Bannerler',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Brand ady:')),
                ('image', models.ImageField(upload_to='brand/', verbose_name='Brand logo:')),
            ],
            options={
                'verbose_name_plural': 'Brendler',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Kategoriya ady:')),
                ('status', models.BooleanField(default=False, verbose_name='Bas sahypada gorkez:')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Saher ady:')),
            ],
            options={
                'verbose_name_plural': 'Şäherler',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ady:')),
                ('lastName', models.CharField(max_length=255, verbose_name='Familýasy:')),
                ('message', models.TextField(verbose_name='Haty:')),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.TextField(verbose_name='Şert ýazyň:')),
            ],
            options={
                'verbose_name_plural': 'Çalşyp bermek şertleri',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Kop soralyan sorag(Bu sahypa name is etyar?):')),
                ('answer', models.TextField(verbose_name='Soragy jogaby:')),
            ],
            options={
                'verbose_name_plural': 'Kömek(Soraglar üçin)',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Menu ady:')),
                ('status', models.BooleanField(default=False, verbose_name='Bas sahypada gorkez:')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Menular',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productCode', models.CharField(max_length=200, verbose_name='Haryt kody:')),
                ('productName', models.CharField(max_length=200, verbose_name='Haryt ady:')),
                ('description', models.TextField(verbose_name='Haryt dusundirisi:')),
                ('price', models.FloatField(verbose_name='Haryt taze baha:')),
                ('oldPrice', models.FloatField(verbose_name='Haryt kone baha:')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Haryt suraty:')),
                ('status', models.BooleanField(default=False, verbose_name='Hayrt yagdayy:')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand', verbose_name='Brand ady:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Kategoriya ady:')),
            ],
            options={
                'verbose_name_plural': 'Harytlar',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Halananlar',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250, verbose_name='Teswir:')),
                ('rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Teswir yazylan haryt:')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Teswir yazan:')),
            ],
            options={
                'verbose_name_plural': 'Teswirler',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product/', verbose_name='Suratlary saylan:')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Haryt saylan:')),
            ],
            options={
                'verbose_name_plural': 'Haryt Suratlary',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productCode', models.CharField(default='', max_length=100000)),
                ('productBrand', models.CharField(default='', max_length=100000)),
                ('product', models.CharField(default='', max_length=100000)),
                ('productDesc', models.CharField(default='', max_length=100000)),
                ('productImage', models.CharField(default='', max_length=100000)),
                ('quantity', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('total', models.CharField(default='', max_length=1000000)),
                ('adress', models.TextField(default='')),
                ('payment_choices', models.CharField(choices=[('NAGT TÖLEG', 'NAGT TÖLEG'), ('KARTDAN TÖLEG', 'KARTDAN TÖLEG')], default='NAGT TÖLEG', max_length=20)),
                ('status', models.CharField(choices=[('Kabul edildi', 'Kabul edildi'), ('Taýýarlanýar', 'Taýýarlanýar'), ('Ugradyldy', 'Ugradyldy'), ('Gowşuruldy', 'Gowşuruldy'), ('Kabul edilmedi', 'Kabul edilmedi'), ('Garaşylýar', 'Garaşylýar')], default='Garaşylýar', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sargytlar',
            },
        ),
        migrations.CreateModel(
            name='Etrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Etrap ady:')),
                ('toleg', models.PositiveIntegerField(default=0, verbose_name='Yol tolegi:')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.city')),
            ],
            options={
                'verbose_name_plural': 'Etraplar',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.menu', verbose_name='Menu sayla:'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sebetler',
            },
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.city')),
                ('city_etrap', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.etrap')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Salgylar',
            },
        ),
    ]
