# Generated by Ginger 5.3.4 on 2024-06-10 16:05

from ginger.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='has_cab_service',
            field=models.BooleanField(null=True, verbose_name=False),
        ),
    ]