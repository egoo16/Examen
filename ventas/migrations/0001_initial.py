# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=7)),
                ('nombre', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='imagen/')),
                ('marca', models.CharField(max_length=2, choices=[('LA', 'Lala'), ('SE', 'Selada'), ('RE', 'Real'), ('CL', 'Cola')], default='LA')),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2)),
                ('Existencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('dpi', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=60)),
                ('productos', models.ManyToManyField(through='ventas.Compra', to='ventas.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(to='ventas.Producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(to='ventas.Usuario'),
        ),
    ]
