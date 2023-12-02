# Generated by Django 4.2.6 on 2023-12-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_requestsnack_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestsnack',
            name='status',
            field=models.CharField(blank=True, choices=[('aprovado', 'aprovado'), ('reprovado', 'reprovado'), ('pendente', 'pendente')], default='pendente', max_length=15, null=True, verbose_name='Situação'),
        ),
    ]
