# Generated by Django 4.2.6 on 2023-11-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('pais', 'apelativo')},
        ),
        migrations.AddConstraint(
            model_name='persona',
            constraint=models.CheckConstraint(check=models.Q(('edad__gte', 18)), name='edad_mayor_18'),
        ),
    ]
