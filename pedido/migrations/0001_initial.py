# Generated by Django 3.0.8 on 2020-09-06 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(verbose_name='Data do Pedido')),
                ('nome_cliente', models.CharField(max_length=255, verbose_name='Nome do Cliente')),
                ('data_entrega', models.DateTimeField(verbose_name='Data de Entrega')),
                ('forma_pagamento', models.CharField(choices=[('D', 'Dinheiro'), ('T', 'Transferência'), ('P', 'PicPay')], max_length=1, verbose_name='Formas de Pagamento')),
                ('pago', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Pago ?')),
                ('entregue', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Entregue ?')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200, verbose_name='Nome do Produto')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('custo', models.FloatField(verbose_name='Custo')),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observações')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido')),
            ],
        ),
    ]
