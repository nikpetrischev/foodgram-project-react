# Generated by Django 3.2.3 on 2024-02-17 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribe_to', to=settings.AUTH_USER_MODEL)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, through='users.Subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
        migrations.AddConstraint(
            model_name='subscriptions',
            constraint=models.UniqueConstraint(fields=('subscriber', 'subscribe_to'), name='unique_subscription'),
        ),
        migrations.AddConstraint(
            model_name='subscriptions',
            constraint=models.CheckConstraint(check=models.Q(('subscriber', django.db.models.expressions.F('subscribe_to')), _negated=True), name='self_subscription'),
        ),
    ]
