# Generated by Django 3.1.1 on 2020-09-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20200920_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecustomer',
            name='stripeSubscriptionId',
            field=models.CharField(default='sub_I3YLps8ZdW5oTz', max_length=255),
            preserve_default=False,
        ),
    ]