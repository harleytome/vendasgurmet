# Generated by Django 3.0.8 on 2020-08-25 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=40, null=True, verbose_name='Bairro')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2, verbose_name='Estado')),
            ],
        ),
    ]