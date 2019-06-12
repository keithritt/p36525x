# Generated by Django 2.2.2 on 2019-06-12 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_auto_20190612_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField()),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='count',
            new_name='reps',
        ),
        migrations.DeleteModel(
            name='Rep',
        ),
    ]
