# Generated by Django 4.2.2 on 2023-07-26 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPage',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('PageName', models.CharField(max_length=50)),
                ('PageNumb', models.IntegerField()),
                ('Page_Duretions', models.DateField()),
            ],
        ),
    ]
