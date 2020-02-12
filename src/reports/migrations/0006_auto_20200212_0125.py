# Generated by Django 2.2 on 2020-02-12 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20200212_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='problemreported',
            name='report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reports.Report'),
            preserve_default=False,
        ),
    ]
